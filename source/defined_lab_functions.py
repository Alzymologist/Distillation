from uncertainties import ufloat # Floating numbers with uncertainty

#### Conventions for functions in this file ####
# If there are messages, function will return (value, messages: list[str]) tuple.
# If tuple is returned by function, it is expected to be (value, messages) tuple.
# Returned values can have type int, float or ufloat for example.
####

range_message = "At least one measurement is outside the expected range."
repeatability_message = "Difference between measurements exceeds the repeatability."
success_message = "Uncertainty was calculated successfully."
quantity_success_message = "Mass is within the expected range."
quantity_warning_message = "Mass is out of the expected range."

def difference(base, deduct):
    return base - deduct

def mass_of_sample_before_distillation(mass_of_flask_with_sample, mass_of_empty_flask):
    difference = mass_of_flask_with_sample - mass_of_empty_flask
    messages = []
    if (99.9 <= difference <= 100.1):
        messages.append(quantity_success_message)
    else:
        messages.append(quantity_warning_message)
    return (difference, messages)

# Function for SGA, SGEA, SGER. Reference:
# Series: Analytica EBC
# Document: 8.2.1 SPECIFIC GRAVITY OF WORT USING A PYKNOMETER – 2004
# Section: 9.1.1 Calculate the specific gravity (SG) of the wort
# SGA = SG of the distillate (references between documents: 9.2.1 -> 9.43.1 -> 8.2.1)
# SGEA = SG of the decarbonated beer (references between documents: 9.2.1 -> 9.43.1 -> 8.2.1)
# SGER = SG of the residue solution (references between documents: 9.4 -> 9.43.1 -> 8.2.1)
def specific_gravity_using_pycnometer(mass_with_substance, mass_empty, mass_with_water):
    return (mass_with_substance - mass_empty) / (mass_with_water - mass_empty)

# Function for alcohol content by mass. Reference:
# Series: Analytica EBC
# Document: 9.2.1 ALCOHOL IN BEER BY DISTILLATION – 2008
# Section: 9.1 Alcohol as % (m/m)
def alcohol_content_by_mass(SGA):
    return 517.4 * (1 - SGA) + 5084 * (1 - SGA)**2 + 33503 * (1 - SGA)**3

# Function for alcohol content by volume (ABV). Reference:
# Series: Analytica EBC
# Document: 9.2.1 ALCOHOL IN BEER BY DISTILLATION – 2008
# Section: 9.2 Alcohol as % (V/V)
def alcohol_content_by_volume(A_by_mass, SGEA):
    return A_by_mass * SGEA / 0.791

# Function for real extract (ER) and apparent extract (EA). Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.1.1 Real extract, 9.1.2 Apparent extract
def extract(specific_gravity):
    return -460.234 + 662.649 * specific_gravity - 202.414 * specific_gravity**2

# Function for original extract. Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.1.4.1 Calculate the original extract (% Plato) of the beer
def original_extract(A_by_mass, real_extract):
    return (2.0665 * A_by_mass + real_extract) * 100 / (100 + 1.0665 * A_by_mass)

# Function for real degree of fermentation of beer (RDF). Reference:
# Series: Analytica EBC
# Document: 9.5 REAL DEGREE OF FERMENTATION OF BEER 1997
# Section: 5.1.1 Calculate real degree of fermentation of beer
def real_degree_of_fermentation(A_by_mass, real_extract):
    return 100 * 2.0665 * A_by_mass / (2.0665 * A_by_mass + real_extract)

# Function for apparent degree of fermentation or apparent attenuation (ADF). Reference:
# Series: Analytica EBC
# Document: 4.11.2 FERMENTABILITY, FINAL ATTENUATION OF LABORATORY WORT FROM MALT: RAPID METHOD – 1999
# Section: 9.1.2 Obtain the fermentability (apparent attenuation)
def apparent_degree_of_fermentation(original_extract, apparent_extract):
    return 100 * (original_extract - apparent_extract) / original_extract

# Function for spirit indication. Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.1.5.1 Calculate the spirit indication (S)
def spirit_indication(SGA):
    return 1000 * (1-SGA)

# Data and function for degrees of gravity lost. Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.1.5.2 Calculate the corresponding degrees of gravity lost (D)
GRAVITY_LOST_RANGES_AND_COEFFICIENTS = [
    ((0, 2), 4.24, 0),
    ((2, 4), 4.38411, -0.32055),
    ((4, 5), 4.4812, -0.70952),
    ((5, 6), 4.5051, -0.81757),
    ((6, 7), 4.54437, -1.05698),
    ((7, 8), 4.55892, -1.16411),
    ((8, 9), 4.57624, -1.30303),
    ((9, 10), 4.5982, -1.50326),
    ((10, 11), 4.71954, -2.72814),
    ((11, 12), 4.8558, -4.2204),
    ((12, 13), 4.9327, -5.1375),
    ((13, 14), 4.9442, -5.2861),
    ((14, 15), 5.0030, -6.0788),
    ((15, 16), 5.0630, -6.97582),
    ((16, float('inf')), 5.07, -7.08),
]

def degrees_of_gravity_lost(S):
    for (lower_bound, upper_bound), A, B in GRAVITY_LOST_RANGES_AND_COEFFICIENTS:
        if lower_bound <= S < upper_bound:
            return S * A + B

# Function for residue gravity (RG). Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.1.5.3 Calculate the residue gravity (RG)
def residue_gravity(SGER):
    return 1000 * (SGER-1)

# Function for original gravity. Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.1.5.4 Calculate the original gravity
def original_gravity(D, RG):
    return D + RG

#### Statistics section ####
# Functions in this section calculate averages and statistical results. Below is information about repeatability limit (represented by variable r95 in this file), reproducibility limit (represented by variable R95 in this file), and expanded uncertainty (represented by variable expanded_uncertainty in this file).

# r95 represents the repeatability limit at the 95 % probability level. Reference:
# Series: Analytica EBC
# Document: 14.2 COLLABORATIVE TRIAL TO DETERMINE THE PRECISION OF A MEASUREMENT METHOD - 2002
# Section: 7.3.5 The repeatability limit at the 95 % probability level

# R95 represents the reproducibility limit at the 95 % probability level. Reference:
# Series: Analytica EBC
# Document: 14.2 COLLABORATIVE TRIAL TO DETERMINE THE PRECISION OF A MEASUREMENT METHOD - 2002
# Section: 7.3.6 The reproducibility limit at the 95 % probability level.

# uE = uE2r / 2.8, where uE is an uncertainty from maximum tolerable bias, and uE2r is a reproducibility limit. Reference:
# Document: Eurolab Technical Report 1/2007 – Measurement uncertainty revisited
# Chapter: 4, Examples. EXAMPLE 7: ROCKWELL HARDNESS TESTING
# Section: 2.1 Measurement uncertainty evaluations derived from indirect calibration

# Multiplication of standard uncertainty u with coverage factor k = 2 yields an expanded uncertainty. Expanded uncertainty can be used to construct a 95 % coverage interval. Reference:
# Document: Eurolab Technical Report 1/2007 – Measurement uncertainty revisited
# Chapter: 1, Review of uncertainty evaluation
# Sections: 1.2 UNCERTAINTY DATA OBTAINED FROM THE VARIOUS APPROACHES, 1.2.1 Modelling approach

# Also see reference:
# Document: IS0 5725-6:1994(E) - Accuracy (trueness and precision) of measurement methods and results
# Section: 4.1 Repeatability and reproducibility limits, 4.1.2
####

# Function for average alcohol content by volume. Reference:
# Series: Analytica EBC
# Document: 9.2.1 ALCOHOL IN BEER BY DISTILLATION – 2008
# Section: 10.1 1995/1996 trial Alcohol in % (V/V)
def average_alcohol_content_by_volume(alcohol_content_S1, alcohol_content_S2):
    mean = (alcohol_content_S1 + alcohol_content_S2) / 2
    range_criterion = (0.84 <= alcohol_content_S1 <= 7.27) and (0.84 <= alcohol_content_S2 <= 7.27)
    repeatability_criterion = abs(alcohol_content_S1 - alcohol_content_S2) <= 0.062 # Calulated using r95, the repeatability limit at the 95 % probability level
    messages = []

    if range_criterion and repeatability_criterion:
        messages.append(success_message)
        R95 = 0.07 + 0.02 * mean # Reproducibility limit at the 95 % probability level
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    else:
        if not range_criterion:
            messages.append(range_message)
        if not repeatability_criterion:
            messages.append(repeatability_message)
        return (mean, messages)

# Function for average alcohol content by mass. Reference:
# Series: Analytica EBC
# Document: 9.2.1 ALCOHOL IN BEER BY DISTILLATION – 2008
# Section: 10.2 1996 trial - 10.2.1 Alcohol in % (m/m)
def average_alcohol_content_by_mass(alcohol_content_S1, alcohol_content_S2):
    mean = (alcohol_content_S1 + alcohol_content_S2) / 2
    range_criterion = (1.72 <= alcohol_content_S1 <=7.00) and (1.72 <= alcohol_content_S2 <=7.00)
    repeatability_criterion = abs(alcohol_content_S1 - alcohol_content_S2) <= 0.03 + 0.005 * mean # Calulated using r95, the repeatability limit at the 95 % probability level
    messages = []

    if range_criterion and repeatability_criterion:
        messages.append(success_message)
        R95 = 0.03 + 0.02 * mean
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    else:
        if not range_criterion:
            messages.append(range_message)
        if not repeatability_criterion:
            messages.append(repeatability_message)
        return (mean, messages)

# Function for average specific gravity. Reference:
# Series: Analytica EBC
# Document: 8.2.1 SPECIFIC GRAVITY OF WORT USING A PYKNOMETER – 2004
# Section: 8.2.2 Carry out duplicate determinations
def average_specific_gravity_of_beer(specific_gravity_S1, specific_gravity_S2):
    mean = (specific_gravity_S1 + specific_gravity_S2) / 2
    repeatability_criterion = abs(round(specific_gravity_S1, 4) - round(specific_gravity_S2, 4)) <= 0.0002 # Calulated using r95, the repeatability limit at the 95 % probability level
    messages = []

    if repeatability_criterion:
        return mean
    else:
        messages.append(repeatability_message)
        return (mean, messages)

# Function for average real extract. Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.2.1.1 Real extract, % Plato
def average_real_extract(real_extract_S1, real_extract_S2):
    mean = (real_extract_S1 + real_extract_S2) / 2
    range_criterion = (2.9 <= real_extract_S1 <= 6.0) and (2.9 <= real_extract_S2 <= 6.0)
    repeatability_criterion = abs(real_extract_S1 - real_extract_S2) <= 0.02 # Calulated using r95, the repeatability limit at the 95 % probability level
    messages = []

    if range_criterion and repeatability_criterion:
        messages.append(success_message)
        R95 = 0.02 * mean
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    else:
        if not range_criterion:
            messages.append(range_message)
        if not repeatability_criterion:
            messages.append(repeatability_message)
        return (mean, messages)

# Function for average original extract. Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.2.1.2 Original extract, % Plato
def average_original_extract(original_extract_S1, original_extract_S2):
    mean = (original_extract_S1 + original_extract_S2) / 2
    range1_criterion = (7 <= original_extract_S1 <= 12) and (7 <= original_extract_S2 <= 12)
    range2_criterion = (round(mean, 1) == 19.0)
    repeatability_for_range1_criterion = abs(original_extract_S1 - original_extract_S2) <= 0.07 # Calulated using r95, the repeatability limit at the 95 % probability level
    repeatability_for_range2_criterion = abs(original_extract_S1 - original_extract_S2) <= 0.15
    messages = []

    if (range1_criterion and repeatability_for_range1_criterion):
        messages.append(success_message)
        R95 = 0.19
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    elif (range2_criterion and repeatability_for_range2_criterion):
        messages.append(success_message)
        R95 = 0.38
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    else:
        if not (range1_criterion or range2_criterion):
            messages.append(range_message)
        if (not range2_criterion) and (not repeatability_for_range1_criterion) \
        or range2_criterion and (not repeatability_for_range2_criterion): # Repeatability for range1 is used as criterion if not in range2.
            messages.append(repeatability_message)
        return (mean, messages)

# Function for average apparent extract. Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.2.1.3 Apparent extract, % Plato
def average_apparent_extract(apparent_extract_S1, apparent_extract_S2):
    mean = (apparent_extract_S1 + apparent_extract_S2) / 2
    range_criterion = (1.5 <= apparent_extract_S1 <= 3.0) and (1.5 <= apparent_extract_S2 <= 3.0)
    repeatability_criterion = abs(apparent_extract_S1 - apparent_extract_S2) <=  0.018 # Calulated using r95, the repeatability limit at the 95 % probability level
    messages = []

    if range_criterion and repeatability_criterion:
        messages.append(success_message)
        R95 = 0.080
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    else:
        if not range_criterion:
            messages.append(range_message)
        if not repeatability_criterion:
            messages.append(repeatability_message)
        return (mean, messages)

# Function for average original gravity. Reference:
# Series: Analytica EBC
# Document: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004
# Section: 9.2.2 The precision values for original gravity (ºSacch.)
def average_original_gravity(original_gravity_S1, original_gravity_S2):
    mean = (original_gravity_S1 + original_gravity_S2) / 2
    range_criterion = (31 <= original_gravity_S1 <= 34) and (31 <= original_gravity_S2 <= 34)
    repeatability_criterion = abs(original_gravity_S1 - original_gravity_S2) <= 0.53 # Calulated using r95, the repeatability limit at the 95 % probability level
    messages = []

    if range_criterion and repeatability_criterion:
        messages.append(success_message)
        R95 = 1.11
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    else:
        if not range_criterion:
            messages.append(range_message)
        if not repeatability_criterion:
            messages.append(repeatability_message)
        return (mean, messages)

# Function for average real degree of fermentation of beer (RDF). Reference:
# Series: Analytica EBC
# Document: 9.5 REAL DEGREE OF FERMENTATION OF BEER 1997
# Section: 5.2.2 Real degree of fermentation %
def average_real_degree_of_fermentation (real_degree_of_fermentation_S1, real_degree_of_fermentation_S2):
    mean = (real_degree_of_fermentation_S1 + real_degree_of_fermentation_S2) / 2
    range1_criterion = (63 <= real_degree_of_fermentation_S1 <= 71) and (63 <= real_degree_of_fermentation_S2 <= 71)
    range2_criterion = (round(mean, 1) == 50.0)
    repeatability_for_range1_criterion = abs(real_degree_of_fermentation_S1 - real_degree_of_fermentation_S2) <= 0.21 # Calulated using r95, the repeatability limit at the 95 % probability level
    repeatability_for_range2_criterion = abs(real_degree_of_fermentation_S1 - real_degree_of_fermentation_S2) <= 0.50
    messages = []

    if (range1_criterion and repeatability_for_range1_criterion):
        messages.append(success_message)
        R95 = 0.61
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    elif (range2_criterion and repeatability_for_range2_criterion):
        messages.append(success_message)
        R95 =  1.16
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    else:
        if not (range1_criterion or range2_criterion):
            messages.append(range_message)
        if (not range2_criterion) and (not repeatability_for_range1_criterion) \
        or range2_criterion and (not repeatability_for_range2_criterion): # Repeatability for range1 is used as criterion if not in range2.
            messages.append(repeatability_message)
        return (mean, messages)

# Function for pH. Reference:
# Series: Analytica EBC
# Document: 9.35 PH OF BEER (FORMERLY PUBLISHED AS IOB METHOD 9.42) – 2004
# Section: 8.2 Precision values determined by IOB Analysis Committee
def average_beer_pH(pH_S1, pH_S2):
    mean = (pH_S1 + pH_S2) / 2
    range_criterion = (3.94 <= pH_S1 <= 4.42) and (3.94 <= pH_S2 <= 4.42 )
    repeatability_criterion = abs(pH_S1 - pH_S2) <= 0.25 # Calulated using r95, the repeatability limit at the 95 % probability level
    messages = []

    if range_criterion and repeatability_criterion:
        messages.append(success_message)
        R95 = 0.133
        expanded_uncertainty = (R95 / 2.8) * 2 # Expanded uncertainty with coverage factor = 2
        return (ufloat(mean, expanded_uncertainty), messages)
    else:
        if not range_criterion:
            messages.append(range_message)
        if not repeatability_criterion:
            messages.append(repeatability_message)
        return (mean, messages)


def average_apparent_degree_of_fermentation(apparent_degree_of_fermentation_S1, apparent_degree_of_fermentation_S2):
    return (apparent_degree_of_fermentation_S1 + apparent_degree_of_fermentation_S2) /2
