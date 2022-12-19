import ipywidgets as widgets

common_width = "500px"
common_description_width = "125px"

date_of_analysis = widgets.DatePicker(
    description="Date of Analysis",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

experiment_id = widgets.Text(
    description="Experiment ID",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

analyst_name = widgets.Dropdown(
    description="Analyst name",
    options=["", "D. Nechaeva", "S. Raik", "E. Barannik"],
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

product_name = widgets.Text(
    description="Product name",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

producer = widgets.Text(
    description="Producer",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

lot = widgets.Text(
    description="Lot",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

declared_alcoholic_strength = widgets.Text(
    description="Declared ABV, %",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

quantity_of_sample = widgets.Text(
    description="Quantity of sample",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

comments = widgets.Text(
    description="Comments",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

submitting_company = widgets.Text(
    description="Submitting company",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

address = widgets.Text(
    description="Company address",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

contact_person = widgets.Text(
    description="Contact person",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

phone_and_email_of_contact_person = widgets.Text(
    description="Phone and e-mail",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)
    
sampler = widgets.Text(
    description="Sampler",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

date_of_sampling = widgets.DatePicker(
    description="Date of sampling",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

date_of_arrival = widgets.DatePicker(
    description="Date of arrival",
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

purpose_of_testing = widgets.Dropdown(
    description="Purpose of testing",
    options=["", "self-control"],
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

results_sending_method = widgets.Dropdown(
    description="Results will be sent",
    options=["", " via e-mail", " by mail", " by courier"],
    style=dict(description_width=common_description_width),
    layout=dict(width=common_width),
)

tag_selector = widgets.TagsInput(
    description="Choose data for report",
    allow_duplicates=False,
    allowed_tags = [] # Allowed tags will be listed dynamically to avoid repetition and keep consistency (see "tag_names").
)

generate_pdf_button = widgets.Button(
    description="Create report",
    button_style='info',
    tooltip='Creates a PDF report with selected data.',
)

# Lab widgets for Series #1

mass_of_distillation_flask_empty_S1 = widgets.FloatText(
    description='Mass of distillation flask (empty), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_distillation_flask_with_sample_S1 = widgets.FloatText(
    description='Mass of distillation flask (with sample), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_distillation_flask_after_distillation_S1 = widgets.FloatText(
    description='Mass of distillation flask (after distillation), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_50ml_of_water_added_to_distillation_flask_S1 = widgets.Dropdown(
    description="Was 50 ml of water added to distillation flask?",
    options=["", True, False],
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_receiver_flask_empty_S1 = widgets.FloatText(
    description='Mass of receiver flask (empty), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_receiver_flask_after_distillation_S1 = widgets.FloatText(
    description='Mass of receiver flask (after distillation), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_5ml_of_water_added_to_receiver_flask_S1  = widgets.Dropdown(
    description="Was 5 ml of water added to receiver flask?",
    options=["", True, False],
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

temperature_in_condenser_S1 = widgets.IntSlider(
    description="Temperature in condenser, °C",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
    step=1,
    min=0,
    max=25,
)

temperature_in_receiver_bath_S1 = widgets.IntSlider(
    description="Temperature in receiver bath, °C",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
    step=1,
    min=0,
    max=25,
)

was_temperature_of_thermostatic_bath_20C_S1 = widgets.Checkbox(
    description="Was the temperature of thermostatic bath  20.0 °C ?",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_distillation_time_30_to_60_min_S1 = widgets.Checkbox(
    description="Was distillation time 30-60 minutes?",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

pycnometer_number_S1 = widgets.FloatText(
    description="Pycnometer number (Series 1)",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_empty_S1 = widgets.FloatText(
    description='Mass of pycnometer (empty), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_with_water_S1 = widgets.FloatText(
    description='Mass of pycnometer (with water), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_with_beer_S1 = widgets.FloatText(
    description='Mass of pycnometer (with beer), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_with_distillate_S1 = widgets.FloatText(
    description='Mass of pycnometer (with distillate), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_with_residue_S1 = widgets.FloatText(
    description='Mass of pycnometer (with residue), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_first_step_of_decarbonisation_done_S1 = widgets.Checkbox(
    description="Was the 1st step of decarbonisation done?",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_second_step_of_decarbonisation_done_S1 = widgets.Checkbox(
    description="Was the 2nd step of decarbonisation done?",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)


beer_pH_S1 = widgets.FloatText(
    description='pH value of the decarbonized beer',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

# Lab widgets for Series #2
# These widgets are copies of widgets for Series 1, but with "_S1" -> "_S2" strings replaced.

mass_of_distillation_flask_empty_S2 = widgets.FloatText(
    description='Mass of distillation flask (empty), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_distillation_flask_with_sample_S2 = widgets.FloatText(
    description='Mass of distillation flask (with sample), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_distillation_flask_after_distillation_S2 = widgets.FloatText(
    description='Mass of distillation flask (after distillation), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_50ml_of_water_added_to_distillation_flask_S2 = widgets.Dropdown(
    description="Was 50 ml of water added to distillation flask?",
    options=["", True, False],
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_receiver_flask_empty_S2 = widgets.FloatText(
    description='Mass of receiver flask (empty), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_receiver_flask_after_distillation_S2 = widgets.FloatText(
    description='Mass of receiver flask (after distillation), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_5ml_of_water_added_to_receiver_flask_S2  = widgets.Dropdown(
    description="Was 5 ml of water added to receiver flask?",
    options=["", True, False],
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

temperature_in_condenser_S2 = widgets.IntSlider(
    description="Temperature in condenser, °C",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
    step=1,
    min=0,
    max=25,
)

temperature_in_receiver_bath_S2 = widgets.IntSlider(
    description="Temperature in receiver bath, °C",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
    step=1,
    min=0,
    max=25,
)

was_temperature_of_thermostatic_bath_20C_S2 = widgets.Checkbox(
    description="Was the temperature of thermostatic bath  20.0 °C ?",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_distillation_time_30_to_60_min_S2 = widgets.Checkbox(
    description="Was distillation time 30-60 minutes?",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

pycnometer_number_S2 = widgets.FloatText(
    description="Pycnometer number (Series 2)",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_empty_S2 = widgets.FloatText(
    description='Mass of pycnometer (empty), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_with_water_S2 = widgets.FloatText(
    description='Mass of pycnometer (with water), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_with_beer_S2 = widgets.FloatText(
    description='Mass of pycnometer (with beer), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_with_distillate_S2 = widgets.FloatText(
    description='Mass of pycnometer (with distillate), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

mass_of_pycnometer_with_residue_S2 = widgets.FloatText(
    description='Mass of pycnometer (with residue), g',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_first_step_of_decarbonisation_done_S2 = widgets.Checkbox(
    description="Was the 1st step of decarbonisation done?",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

was_second_step_of_decarbonisation_done_S2 = widgets.Checkbox(
    description="Was the 2nd step of decarbonisation done?",
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

beer_pH_S2 = widgets.FloatText(
    description='pH value of the decarbonized beer',
    step=0.01,
    style=dict(description_width='initial'),
    layout=dict(width=common_width),
)

# Output widgets.
# These are used to show results inside notebook.

tab1_output = widgets.Textarea(
    layout={'height': '100%', 'width': '95%'}
)

tab1_box = widgets.VBox(
    [tab1_output],
    layout={'height': '580px', 'width': '450px'}
)


tab2_output = widgets.Textarea(
    layout={'height': '100%', 'width': '95%'}
)

tab2_box = widgets.VBox(
    [tab2_output],
    layout={'height': '580px', 'width': '450px'}
)
