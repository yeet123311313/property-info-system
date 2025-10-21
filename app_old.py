from h2o_wave import main, app, Q, ui

@app('/info-sheet')
async def serve(q: Q):
    # Add the page title
    q.page['header'] = ui.header_card(
        box='1 1 12 1',
        title='Property Information Sheet',
        subtitle='',
    )
    
    # Left Column - Property Information (with scrollable content)
    q.page['property_info'] = ui.form_card(
        box='1 2 6 7',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Property Information</span>'),
            ui.textbox(name='address', label='Address', multiline=True),
            ui.textbox(name='google_maps_link', label='Google Maps Link'),
            ui.textbox(name='lot_number', label='Lot Number'),
            ui.textbox(name='borough', label='Borough'),
            ui.textbox(name='year_construction', label='Year of construction'),
            ui.textbox(name='total_building_sf', label='Total Building SF'),
            ui.textbox(name='google_maps_building_sf', label='Google Maps Building SF'),
            ui.textbox(name='floor_plate', label='Floor Plate'),
            ui.textbox(name='land_sf', label='Land SF'),
            ui.textbox(name='ceiling_height', label='Ceiling Height'),
            ui.textbox(name='docks', label='Docks - google or vendor?'),
            ui.textbox(name='column_distance', label='Column Distance'),
            ui.textbox(name='amps', label='Amps'),
        ]
    )
    
    # Right Column - Owner Information (with scrollable content)
    q.page['owner_info'] = ui.form_card(
        box='7 2 6 7',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Owner Information</span>'),
            ui.textbox(name='names_of_owners', label='Names of Owners', multiline=True, height='80px'),
            ui.textbox(name='other_properties', label='Other Properties', multiline=True, height='80px'),
            ui.textbox(name='contact_info', label='Contact Info', multiline=True, height='80px'),
            ui.textbox(name='vendor_goes_by', label='Vendor Goes By'),
        ]
    )
    
    # Left Column - Building Breakdown (with scrollable content)
    q.page['building_breakdown'] = ui.form_card(
        box='1 9 6 5',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Building Breakdown</span>'),
            ui.textbox(name='total_building_sf_breakdown', label='Total Building SF'),
            ui.textbox(name='warehouse_space', label='Warehouse Space'),
            ui.textbox(name='mezzanine_space', label='Mezzanine Space'),
            ui.textbox(name='office_space_sf', label='Office Space SF'),
            ui.textbox(name='percent_office', label='% of Office', value='#DIV/0!'),
        ]
    )
    
    # Right Column - Title (with scrollable content)
    q.page['title_section'] = ui.form_card(
        box='7 9 6 5',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Title</span>'),
            ui.textbox(name='previous_sale_price', label='Previous Sale Price'),
            ui.textbox(name='active_mortgage', label='Active Mortgage'),
            ui.textbox(name='registered_leases', label='Registered Leases'),
            ui.textbox(name='other_notes', label='Other Notes'),
        ]
    )
    
    # Left Column - Our Offer and Vendor's Asking (with scrollable content)
    q.page['offer_section'] = ui.form_card(
        box='1 14 6 6',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Our Offer</span>'),
            ui.textbox(name='purchase_price', label='Purchase Price'),
            ui.textbox(name='price_psf_building', label='Price PSF of Building'),
            ui.textbox(name='price_psf_land', label='Price PSF of Land', value='#DIV/0!'),
            ui.textbox(name='net_rent_psf', label='Net Rent PSF'),
            ui.textbox(name='cap_rate', label='Cap Rate'),
            ui.separator(),
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Vendor\'s Asking</span>'),
            ui.textbox(name='vendor_purchase_price', label='Purchase Price'),
            ui.textbox(name='vendor_price_psf_building', label='Price PSF of Building'),
            ui.textbox(name='vendor_price_psf_land', label='Price PSF of Land', value='#DIV/0!'),
            ui.textbox(name='vendor_net_rent_psf', label='Net Rent PSF'),
            ui.textbox(name='vendor_cap_rate', label='Cap Rate'),
        ]
    )
    
    # Right Column - Important Info (with scrollable content)
    q.page['important_info'] = ui.form_card(
        box='7 14 6 6',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Important Info</span>'),
            ui.textbox(name='sale_conditions', label='Sale Conditions', multiline=True, height='60px'),
            ui.textbox(name='leaseback_terms', label='Leaseback Terms', multiline=True, height='60px'),
            ui.textbox(name='business_for_sale', label='Business for Sale', multiline=True, height='60px'),
            ui.textbox(name='owns_surrounding_lots', label='Owns surrounding lots', multiline=True, height='60px'),
            ui.textbox(name='type_of_property', label='Type of Property', value='See comment for instructions', multiline=True, height='60px'),
        ]
    )
    
    # Left Column - Income (with scrollable content)
    q.page['income'] = ui.form_card(
        box='1 20 6 5',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Income</span>'),
            ui.textbox(name='gross_income_year', label='Gross Income / Year'),
            ui.textbox(name='gross_income_psf', label='Gross Income per Sq Ft'),
            ui.textbox(name='opex_year', label='OPEX / Year'),
            ui.textbox(name='opex_psf', label='OPEX per Sq Ft'),
            ui.textbox(name='net_income_year', label='Net Income / Year', value='$0.00'),
            ui.textbox(name='net_income_psf', label='Net Income per Sq Ft', value='$0.00'),
            ui.textbox(name='occupancy_percent', label='Occupancy %'),
        ]
    )
    
    # Right Column - Questions (with scrollable content)
    q.page['questions'] = ui.form_card(
        box='7 20 6 5',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Questions</span>'),
            ui.textbox(name='questions_text', label='', multiline=True, height='250px'),
        ]
    )
    
    await q.page.save()
