# Property Information System

A web-based property information management system built with H2O Wave. Create unique property sheets with permanent URLs perfect for linking in your CRM.

![Property Information System](https://img.shields.io/badge/Built%20with-H2O%20Wave-blue)
![Deploy](https://img.shields.io/badge/Deploy%20to-Railway-blueviolet)

## Features

- 🏢 **Multiple Properties** - Manage unlimited property information sheets
- 🔗 **Unique URLs** - Each property gets a permanent, shareable link
- 💾 **Auto-Save** - Changes save automatically as you type
- 📊 **Comprehensive Fields** - Property info, owner details, financials, and more
- 🎨 **Clean UI** - Green-themed interface matching traditional info sheets
- 🚀 **Easy Deployment** - Deploy to Railway in minutes
- 💼 **CRM Integration** - Link property URLs directly in your CRM

## Quick Start

### Local Development

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Start the Wave server** (in one terminal):
```bash
# The Wave server should already be downloaded in wave-server/
cd wave-server/wave-0.26.3-windows-amd64
./waved
```

3. **Run the app** (in another terminal):
```bash
python -m h2o_wave run app.py
```

4. **Open your browser**:
```
http://localhost:10101/
```

### Deploy to Railway

See [DEPLOY.md](DEPLOY.md) for complete deployment instructions.

Quick version:
1. Push to GitHub
2. Create new project on [Railway](https://railway.app)
3. Deploy from your GitHub repository
4. Railway auto-detects configuration and deploys

## Property Sheet Sections

Each property information sheet includes:

### Property Information
- Address, location details
- Building specifications (SF, floors, ceiling height)
- Construction year
- Docks, utilities (amps)

### Owner Information
- Owner names
- Contact information
- Other properties owned
- Vendor details

### Building Breakdown
- Total building SF
- Warehouse space
- Mezzanine space
- Office space
- Office percentage

### Title Information
- Previous sale price
- Active mortgages
- Registered leases
- Additional notes

### Financial Details
- **Our Offer**: Purchase price, PSF calculations, cap rate
- **Vendor's Asking**: Their asking price and terms

### Important Information
- Sale conditions
- Leaseback terms
- Business for sale details
- Surrounding lots ownership
- Property type

### Income Analysis
- Gross income (yearly/PSF)
- Operating expenses (yearly/PSF)
- Net income calculations
- Occupancy percentage

### Questions
- Free-form notes and questions

## Usage

### Creating a Property

1. Visit the home page (`/`)
2. Click "+ Create New Property"
3. You'll be redirected to a unique URL like `/property/abc-123-def`
4. Fill in the information - it auto-saves!

### Linking in CRM

1. Copy the property URL (e.g., `https://your-app.railway.app/property/abc-123-def`)
2. Add it to your CRM as a custom field, note, or link
3. Click the link anytime to view/edit the property sheet

### Managing Properties

- **Home page**: See all properties at a glance
- **Search**: Quickly find properties by address
- **Edit**: Click any property to view/edit
- **Auto-save**: No save button needed!

## Tech Stack

- **H2O Wave** - Python web framework
- **SQLite** - Database for property storage
- **Railway** - Cloud deployment platform

## File Structure

```
.
├── app.py              # Main application with routes
├── database.py         # SQLite database operations
├── requirements.txt    # Python dependencies
├── railway.json        # Railway configuration
├── start_railway.sh    # Railway startup script
├── DEPLOY.md          # Deployment guide
├── QUICKSTART.md      # Quick start guide
└── README.md          # This file
```

## Configuration

### Environment Variables

- `PORT` - Railway sets this automatically
- `DATABASE_FILE` - SQLite database path (default: `properties.db`)

### Database

The app uses SQLite by default. For production with Railway, consider upgrading to PostgreSQL:

1. Add PostgreSQL database in Railway
2. Update `database.py` to use PostgreSQL
3. Use Railway's provided connection variables

## Development

### Running Locally

```bash
# Start Wave server
bash start_wave.sh

# Or manually
./wave-server/wave-0.26.3-windows-amd64/waved &
python -m h2o_wave run app.py
```

### Making Changes

The app uses hot-reload - changes are reflected immediately.

## Contributing

This is a private project, but feel free to fork and customize for your needs!

## License

Private/Proprietary

## Support

For issues or questions:
1. Check the deployment logs
2. Review DEPLOY.md
3. Verify all dependencies are installed

## Roadmap

- [ ] PostgreSQL support for Railway
- [ ] Export to PDF/Excel
- [ ] User authentication
- [ ] API for CRM integration
- [ ] Bulk import from CSV
- [ ] Advanced search and filtering
