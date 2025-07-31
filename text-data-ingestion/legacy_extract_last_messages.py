#Updated to use the imessage-exporter library

import sqlite3
import plistlib
import os

def extract_text_from_attributed_body(blob):
    if not blob:
        return None
    bplist_start = blob.find(b'bplist00')
    if bplist_start == -1:
        return None
    try:
        plist = plistlib.loads(blob[bplist_start:])
        objects = plist.get('$objects', [])
        strings = [obj for obj in objects if isinstance(obj, str) and obj.strip()]
        if strings:
            return max(strings, key=len)
        return None
    except Exception as e:
        return f"[Error decoding plist: {e}]"

def main():
    db_path = os.path.join(os.path.dirname(__file__), '../data/chat.db')
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #Get the last 1000 messages by date (descending ROWID is a good proxy for recency)
    cursor.execute("""
        SELECT text, attributedBody, date
        FROM message
        ORDER BY ROWID DESC
        LIMIT 1000;
    """)
    rows = cursor.fetchall()

    for idx, (text, blob, date) in enumerate(rows, 1):
        decoded = extract_text_from_attributed_body(blob) if blob else None
        if decoded:
            msg = decoded
        elif text:
            msg = text
        else:
            msg = '[No text found]'
        print(f"{idx}. {msg}")

    conn.close()

if __name__ == "__main__":
    main() 