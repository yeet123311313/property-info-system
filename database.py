import sqlite3
import uuid
from datetime import datetime
import json
from typing import Optional, Dict, List

DATABASE_FILE = 'properties.db'

def init_db():
    """Initialize the database with the properties table"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS properties (
            id TEXT PRIMARY KEY,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def create_property() -> str:
    """Create a new property and return its unique ID"""
    property_id = str(uuid.uuid4())
    now = datetime.utcnow().isoformat()
    
    empty_data = {}
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO properties (id, created_at, updated_at, data) VALUES (?, ?, ?, ?)',
        (property_id, now, now, json.dumps(empty_data))
    )
    
    conn.commit()
    conn.close()
    
    return property_id

def get_property(property_id: str) -> Optional[Dict]:
    """Get property data by ID"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT data FROM properties WHERE id = ?', (property_id,))
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return json.loads(row[0])
    return None

def save_property(property_id: str, data: Dict):
    """Save property data"""
    now = datetime.utcnow().isoformat()
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute(
        'UPDATE properties SET updated_at = ?, data = ? WHERE id = ?',
        (now, json.dumps(data), property_id)
    )
    
    conn.commit()
    conn.close()

def list_properties() -> List[Dict]:
    """List all properties with their IDs and basic info"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, created_at, updated_at, data FROM properties ORDER BY created_at DESC')
    rows = cursor.fetchall()
    
    conn.close()
    
    properties = []
    for row in rows:
        data = json.loads(row[3])
        properties.append({
            'id': row[0],
            'created_at': row[1],
            'updated_at': row[2],
            'address': data.get('address', 'No address'),
        })
    
    return properties

def delete_property(property_id: str):
    """Delete a property by ID"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM properties WHERE id = ?', (property_id,))
    
    conn.commit()
    conn.close()
