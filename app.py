from h2o_wave import main, app, Q, ui
from database import init_db, create_property, get_property, save_property, list_properties, delete_property

# Initialize database on startup
init_db()

@app('/')
async def serve(q: Q):
    """Main app handler - routes to home or property page based on args"""
    
    # Check if URL has a hash parameter for direct property link
    # This enables shareable URLs like https://your-app.railway.app/#property_id=abc-123
    if q.args['#'] and q.args['#'].startswith('property_id='):
        property_id_from_hash = q.args['#'].replace('property_id=', '')
        if property_id_from_hash and not q.args.go_home:
            await show_property(q, property_id_from_hash)
            return
    
    # Check if going back home (must be first to override other args)
    if q.args.go_home:
        q.client.property_id = None  # Clear property ID
        q.client.initialized = False  # Reset client state
        await show_home(q)
        return
    
    # Check if we're viewing a specific property
    if q.args.property_id:
        await show_property(q, q.args.property_id)
        return
    
    # Check if we're creating a new property
    if q.args.create_new:
        property_id = create_property()
        # Show the property page for the new property
        await show_property(q, property_id)
        return
    
    # Default: show home page
    await show_home(q)

async def show_home(q: Q):
    """Home page - list all properties and create new ones"""
    
    # Clear all existing cards to ensure clean state
    q.page.drop()
    
    # Get all properties
    properties = list_properties()
    
    # Build property list items
    property_items = []
    for prop in properties:
        property_items.append(
            ui.text(f"**{prop['address'] or 'Unnamed Property'}**"),
        )
        property_items.append(
            ui.text(f"ID: {prop['id'][:8]}... | Created: {prop['created_at'][:10]} | Updated: {prop['updated_at'][:10]}"),
        )
        property_items.append(
            ui.button(name=f'property_id', value=prop['id'], label='View/Edit', primary=True),
        )
        property_items.append(ui.separator())
    
    if not property_items:
        property_items.append(ui.text('No properties yet. Create your first property!'))
    
    q.page['meta'] = ui.meta_card(box='', title='Property Information System')
    
    q.page['header'] = ui.header_card(
        box='1 1 12 1',
        title='Property Information System',
        subtitle='Manage all your property information sheets',
    )
    
    q.page['content'] = ui.form_card(
        box='1 2 12 -1',
        items=[
            ui.text_xl('Property Information System'),
            ui.text('Create and manage property information sheets with unique URLs.'),
            ui.separator(),
            ui.button(name='create_new', label='+ Create New Property', primary=True),
            ui.separator(),
            ui.text_l('Your Properties:'),
            *property_items,
        ]
    )
    
    await q.page.save()

async def show_property(q: Q, property_id: str):
    """Property information sheet for a specific property"""
    
    # Clear all existing cards to ensure clean state
    q.page.drop()
    
    # Initialize client storage for property data if needed
    if not q.client.initialized or q.client.property_id != property_id:
        data = get_property(property_id)
        if data is None:
            # Property not found
            q.page['meta'] = ui.meta_card(box='', title='Property Not Found')
            q.page['error'] = ui.form_card(
                box='1 1 12 -1',
                items=[
                    ui.text_xl('Property not found!'),
                    ui.button(name='go_home', label='← Back to Home', primary=True),
                ]
            )
            await q.page.save()
            return
        
        q.client.property_id = property_id
        q.client.initialized = True
        q.client.data = data
    
    # Handle form submission (auto-save on any change)
    # Convert q.args to dict to iterate
    args_dict = {k: v for k, v in vars(q.args).items() if not k.startswith('_')}
    
    for key, value in args_dict.items():
        if key not in ['property_id', 'go_home', 'create_new'] and value is not None and value != '':
            q.client.data[key] = value
    
    # Save to database if there were changes
    if args_dict:
        save_property(q.client.property_id, q.client.data)
    
    # Get current data
    data = q.client.data
    
    # Build shareable URL
    # When deployed, this will be like: https://your-app.railway.app/#property_id=abc-123
    base_url = q.app.url if hasattr(q.app, 'url') else 'http://localhost:10101'
    shareable_url = f"{base_url}/#property_id={property_id}"
    
    # Build the property sheet UI
    q.page['meta'] = ui.meta_card(
        box='',
        title=f'Property: {data.get("address", "Info Sheet")}',
        layouts=[
            ui.layout(breakpoint='xs', zones=[
                ui.zone('header'),
                ui.zone('url_card'),
                ui.zone('content', direction=ui.ZoneDirection.ROW, zones=[
                    ui.zone('left', size='50%'),
                    ui.zone('right', size='50%'),
                ])
            ])
        ]
    )
    
    q.page['header'] = ui.header_card(
        box='header',
        title='Property Information Sheet',
        subtitle=f'Property ID: {property_id[:8]}...',
        items=[ui.button(name='go_home', label='← Back to List')]
    )
    
    # Add URL card showing the shareable link
    q.page['url_card'] = ui.form_card(
        box='url_card',
        items=[
            ui.text(f'**Shareable URL for CRM:** Copy this link to use in your CRM'),
            ui.textbox(name='shareable_url_display', label='', value=shareable_url, readonly=True),
            ui.text('_This URL will work when deployed to Railway. Each property has a permanent unique link._'),
        ]
    )
    
    # Left Column - Property Information
    q.page['property_info'] = ui.form_card(
        box='1 2 6 7',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Property Information</span>'),
            ui.textbox(name='address', label='Address', multiline=True, value=data.get('address', ''), trigger=True),
            ui.textbox(name='google_maps_link', label='Google Maps Link', value=data.get('google_maps_link', ''), trigger=True),
            ui.textbox(name='lot_number', label='Lot Number', value=data.get('lot_number', ''), trigger=True),
            ui.textbox(name='borough', label='Borough', value=data.get('borough', ''), trigger=True),
            ui.textbox(name='year_construction', label='Year of construction', value=data.get('year_construction', ''), trigger=True),
            ui.textbox(name='total_building_sf', label='Total Building SF', value=data.get('total_building_sf', ''), trigger=True),
            ui.textbox(name='google_maps_building_sf', label='Google Maps Building SF', value=data.get('google_maps_building_sf', ''), trigger=True),
            ui.textbox(name='floor_plate', label='Floor Plate', value=data.get('floor_plate', ''), trigger=True),
            ui.textbox(name='land_sf', label='Land SF', value=data.get('land_sf', ''), trigger=True),
            ui.textbox(name='ceiling_height', label='Ceiling Height', value=data.get('ceiling_height', ''), trigger=True),
            ui.textbox(name='docks', label='Docks - google or vendor?', value=data.get('docks', ''), trigger=True),
            ui.textbox(name='column_distance', label='Column Distance', value=data.get('column_distance', ''), trigger=True),
            ui.textbox(name='amps', label='Amps', value=data.get('amps', ''), trigger=True),
        ]
    )
    
    # Right Column - Owner Information
    q.page['owner_info'] = ui.form_card(
        box='7 2 6 7',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Owner Information</span>'),
            ui.textbox(name='names_of_owners', label='Names of Owners', multiline=True, height='80px', value=data.get('names_of_owners', ''), trigger=True),
            ui.textbox(name='other_properties', label='Other Properties', multiline=True, height='80px', value=data.get('other_properties', ''), trigger=True),
            ui.textbox(name='contact_info', label='Contact Info', multiline=True, height='80px', value=data.get('contact_info', ''), trigger=True),
            ui.textbox(name='vendor_goes_by', label='Vendor Goes By', value=data.get('vendor_goes_by', ''), trigger=True),
        ]
    )
    
    # Left Column - Building Breakdown
    q.page['building_breakdown'] = ui.form_card(
        box='1 9 6 5',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Building Breakdown</span>'),
            ui.textbox(name='total_building_sf_breakdown', label='Total Building SF', value=data.get('total_building_sf_breakdown', ''), trigger=True),
            ui.textbox(name='warehouse_space', label='Warehouse Space', value=data.get('warehouse_space', ''), trigger=True),
            ui.textbox(name='mezzanine_space', label='Mezzanine Space', value=data.get('mezzanine_space', ''), trigger=True),
            ui.textbox(name='office_space_sf', label='Office Space SF', value=data.get('office_space_sf', ''), trigger=True),
            ui.textbox(name='percent_office', label='% of Office', value=data.get('percent_office', '#DIV/0!'), trigger=True),
        ]
    )
    
    # Right Column - Title
    q.page['title_section'] = ui.form_card(
        box='7 9 6 5',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Title</span>'),
            ui.textbox(name='previous_sale_price', label='Previous Sale Price', value=data.get('previous_sale_price', ''), trigger=True),
            ui.textbox(name='active_mortgage', label='Active Mortgage', value=data.get('active_mortgage', ''), trigger=True),
            ui.textbox(name='registered_leases', label='Registered Leases', value=data.get('registered_leases', ''), trigger=True),
            ui.textbox(name='other_notes', label='Other Notes', value=data.get('other_notes', ''), trigger=True),
        ]
    )
    
    # Left Column - Our Offer and Vendor's Asking
    q.page['offer_section'] = ui.form_card(
        box='1 14 6 6',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Our Offer</span>'),
            ui.textbox(name='purchase_price', label='Purchase Price', value=data.get('purchase_price', ''), trigger=True),
            ui.textbox(name='price_psf_building', label='Price PSF of Building', value=data.get('price_psf_building', ''), trigger=True),
            ui.textbox(name='price_psf_land', label='Price PSF of Land', value=data.get('price_psf_land', '#DIV/0!'), trigger=True),
            ui.textbox(name='net_rent_psf', label='Net Rent PSF', value=data.get('net_rent_psf', ''), trigger=True),
            ui.textbox(name='cap_rate', label='Cap Rate', value=data.get('cap_rate', ''), trigger=True),
            ui.separator(),
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Vendor\'s Asking</span>'),
            ui.textbox(name='vendor_purchase_price', label='Purchase Price', value=data.get('vendor_purchase_price', ''), trigger=True),
            ui.textbox(name='vendor_price_psf_building', label='Price PSF of Building', value=data.get('vendor_price_psf_building', ''), trigger=True),
            ui.textbox(name='vendor_price_psf_land', label='Price PSF of Land', value=data.get('vendor_price_psf_land', '#DIV/0!'), trigger=True),
            ui.textbox(name='vendor_net_rent_psf', label='Net Rent PSF', value=data.get('vendor_net_rent_psf', ''), trigger=True),
            ui.textbox(name='vendor_cap_rate', label='Cap Rate', value=data.get('vendor_cap_rate', ''), trigger=True),
        ]
    )
    
    # Right Column - Important Info
    q.page['important_info'] = ui.form_card(
        box='7 14 6 6',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Important Info</span>'),
            ui.textbox(name='sale_conditions', label='Sale Conditions', multiline=True, height='60px', value=data.get('sale_conditions', ''), trigger=True),
            ui.textbox(name='leaseback_terms', label='Leaseback Terms', multiline=True, height='60px', value=data.get('leaseback_terms', ''), trigger=True),
            ui.textbox(name='business_for_sale', label='Business for Sale', multiline=True, height='60px', value=data.get('business_for_sale', ''), trigger=True),
            ui.textbox(name='owns_surrounding_lots', label='Owns surrounding lots', multiline=True, height='60px', value=data.get('owns_surrounding_lots', ''), trigger=True),
            ui.textbox(name='type_of_property', label='Type of Property', value=data.get('type_of_property', 'See comment for instructions'), multiline=True, height='60px', trigger=True),
        ]
    )
    
    # Left Column - Income
    q.page['income'] = ui.form_card(
        box='1 20 6 5',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Income</span>'),
            ui.textbox(name='gross_income_year', label='Gross Income / Year', value=data.get('gross_income_year', ''), trigger=True),
            ui.textbox(name='gross_income_psf', label='Gross Income per Sq Ft', value=data.get('gross_income_psf', ''), trigger=True),
            ui.textbox(name='opex_year', label='OPEX / Year', value=data.get('opex_year', ''), trigger=True),
            ui.textbox(name='opex_psf', label='OPEX per Sq Ft', value=data.get('opex_psf', ''), trigger=True),
            ui.textbox(name='net_income_year', label='Net Income / Year', value=data.get('net_income_year', '$0.00'), trigger=True),
            ui.textbox(name='net_income_psf', label='Net Income per Sq Ft', value=data.get('net_income_psf', '$0.00'), trigger=True),
            ui.textbox(name='occupancy_percent', label='Occupancy %', value=data.get('occupancy_percent', ''), trigger=True),
        ]
    )
    
    # Right Column - Questions
    q.page['questions'] = ui.form_card(
        box='7 20 6 5',
        items=[
            ui.text_xl('<span style="color: white; background-color: #4a7c59; padding: 8px; display: block; text-align: center; font-weight: bold;">Questions</span>'),
            ui.textbox(name='questions_text', label='', multiline=True, height='250px', value=data.get('questions_text', ''), trigger=True),
        ]
    )
    
    await q.page.save()
