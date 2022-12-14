from uncertainties import ufloat # Floating number with uncertainty

def mass_of_sample_before_distillation(mass_dist_flask_with_sample, mass_dist_flask_empty):
    return mass_dist_flask_with_sample - mass_dist_flask_empty

#Sample mass after distillation (100,0±0,1), g
def mass_of_distillate(mass_rec_flask_after_dist, mass_rec_flask_empty):
    return mass_rec_flask_after_dist - mass_rec_flask_empty

#Distilled beer mass after dist., (100,0±0,1) g
def mass_of_residue_after_distillation(mass_dist_flask_after_dist, mass_dist_flask_empty):
    return mass_dist_flask_after_dist - mass_dist_flask_empty

# SGA = specific gravity of the distillate (source: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004)
def specific_gravity_of_distillate(mass_pycn_with_dist, mass_pycn_empty, mass_pycn_with_water):
    return (mass_pycn_with_dist - mass_pycn_empty) / (mass_pycn_with_water -  mass_pycn_empty)

# SGEA = specific gravity of decarbonated beer (source: 9.2.1 ALCOHOL IN BEER BY DISTILLATION)
def specific_gravity_of_beer(mass_pycn_with_beer, mass_pycn_empty, mass_pycn_with_water):
    return (mass_pycn_with_beer - mass_pycn_empty) / (mass_pycn_with_water -  mass_pycn_empty)

# SGER = specific gravity of the residue (source: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004)   
def specific_gravity_of_residue(mass_pycn_with_residue, mass_pycn_empty, mass_pycn_with_water):
    return (mass_pycn_with_residue - mass_pycn_empty) / (mass_pycn_with_water -  mass_pycn_empty)

# A, Alcohol as % (m/m) = Alcohol content of the distillate (source: 9.2.1 ALCOHOL IN BEER BY DISTILLATION)
def alcohol_content_by_mass(SGA):
    return 517.4*(1 - SGA) + 5084*(1 - SGA)**2 + 33503*(1 - SGA)**3 

# ABV, Alcohol as % (V/V)  (source: 9.2.1 ALCOHOL IN BEER BY DISTILLATION)
def alcohol_content_by_volume(A, SGEA):
    return A * SGEA/0.791

#Real extract, ER (% Plato) (9.1.1)
def real_extract(SGER):
    return -460.234 + 662.649 * SGER - 202.414 * SGER**2

#Apparent extract, EA (% Plato) (9.1.2)
def apparent_extract(SGEA):                                          
    return -460.234 + 662.649 * SGEA - 202.414 * SGEA**2

#Original extract, p (% Plato) (9.1.4.1)
def original_extract(A, real_extract):
    return (2.0665 * A + real_extract) * 100 / (100 + 1.0665 * A)

# RDF = real degree of fermentation of beer (source: 9.5 REAL DEGREE OF FERMENTATION OF BEER)
def real_degree_of_fermentation(A, real_extract):
    return 100 * 2.0665 * A / (2.0665 * A + real_extract)

# ADF = Apparent degree of Fermentation 
#(source: Examination of the Relationships Between Original, Real and Apparent Extracts,
# https://doi.org/10.1080/03610470.2018.1553459)
def apparent_degree_of_fermentation(original_extract, apparent_extract):
    return 100 * (original_extract-apparent_extract) / original_extract

# S = Spirit indication (source: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004)
def spirit_indication(SGA):
    return 1000 * (1-SGA)

# D = degrees of gravity lost (source: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004)
def degrees_of_gravity_lost(S):
    if        S < 2:   D = S * 4.24
    elif 2 <= S < 4:   D = S * 4.38411 - 0.32055
    elif 4 <= S < 5:   D = S * 4.4812 - 0.70952
    elif 5 <= S < 6:   D = S * 4.5051 - 0.81757
    elif 6 <= S < 7:   D = S * 4.54437 - 1.05698
    elif 7 <= S < 8:   D = S * 4.55892 - 1.16411
    elif 8 <= S < 9:   D = S * 4.57624 - 1.30303
    elif 9 <= S < 10:  D = S * 4.5982 - 1.50326
    elif 10 <= S < 11: D = S * 4.71954 - 2.72814
    elif 11 <= S < 12: D = S * 4.8558 - 4.2204
    elif 12 <= S < 13: D = S * 4.9327 - 5.1375
    elif 13 <= S < 14: D = S * 4.9442 - 5.2861
    elif 14 <= S < 15: D = S * 5.0030 - 6.0788
    elif 15 <= S < 16: D = S * 5.0630 - 6.97582
    elif       S>= 16: D = S * 5.07 - 7.08
    return D

# RG = Residue Gravity (RG) (source: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004)
def residue_gravity(SGER):
    return 1000 * (SGER-1)

# Original Gravity (º Sacch.) (source: 9.4 ORIGINAL, REAL AND APPARENT EXTRACT AND ORIGINAL GRAVITY OF BEER – 2004)
def original_gravity(D, RG):
    return D + RG

# Series: Analytica EBC
# Document: 9.2.1 ALCOHOL IN BEER BY DISTILLATION – 2008
# Section: 10.1 1995/1996 trial Alcohol in % (V/V)
def average_alcohol_content_by_volume(alcohol_content_S1, alcohol_content_S2):
    mean = (alcohol_content_S1 + alcohol_content_S2) / 2
    repeatability = 0.062
    if  (0.84 <= alcohol_content_S1 <= 7.27) \
    and (0.84 <= alcohol_content_S2 <= 7.27) \
    and (abs(alcohol_content_S1 - alcohol_content_S2) <= repeatability):
        R95 = 0.07 + 0.02 * mean
        uncertainty = (R95 / 2.77) * 2
        return ufloat(mean, uncertainty)
    else:
        return None

# Series: Analytica EBC
# Document: 9.2.1 ALCOHOL IN BEER BY DISTILLATION – 2008
# Section: 10.2 1996 trial - 10.2.1 Alcohol in % (m/m)
def average_alcohol_content_by_mass(alcohol_content_S1, alcohol_content_S2):
    mean = (alcohol_content_S1 + alcohol_content_S2) / 2
    repeatability = 0.03 + 0.005 * mean
    if  (1.72 <= alcohol_content_S1 <=7.00) \
    and (1.72 <= alcohol_content_S2 <=7.00) \
    and (abs(alcohol_content_S1 - alcohol_content_S2) <= repeatability):
        R95 = 0.03 + 0.02 * mean
        uncertainty = (R95 / 2.77) * 2
        return ufloat(mean, uncertainty)
    else:
        return None

def average_specific_gravity_of_beer(specific_gravity_S1, specific_gravity_S2):
    return (specific_gravity_S1 + specific_gravity_S2) / 2

def average_original_extract(original_extract_S1, original_extract_S2):
    return (original_extract_S1 + original_extract_S2) / 2

def average_real_extract(real_extract_S1, real_extract_S2):
    return (real_extract_S1 + real_extract_S2) / 2

def average_apparent_extract(apparent_extract_S1, apparent_extract_S2):
    return (apparent_extract_S1 + apparent_extract_S2) / 2

def average_real_degree_of_fermentation (real_degree_of_fermentation_S1, real_degree_of_fermentation_S2):
    return (real_degree_of_fermentation_S1 + real_degree_of_fermentation_S2) / 2

def average_apparent_degree_of_fermentation(apparent_degree_of_fermentation_S1, apparent_degree_of_fermentation_S2):
    return (apparent_degree_of_fermentation_S1 + apparent_degree_of_fermentation_S2) /2

def average_original_gravity(original_gravity_S1, original_gravity_S2):
    return (original_gravity_S1 + original_gravity_S2) / 2

def average_beer_pH(pH_S1, pH_S2):
    return (pH_S1 + pH_S2) / 2
