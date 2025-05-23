import streamlit as st
import pandas as pd

# --- Titel & Intro ---
st.set_page_config(page_title="SmartKauf – Deine Einkaufsliste", layout="wide")
st.title("🛒 SmartKauf")
st.markdown("Willkommen bei **SmartKauf** – deiner intelligenten Einkaufsliste auf Basis von Kassenbons und Gewohnheiten.")

# --- Statische Einkaufsliste als Startpunkt ---
daten = [
    ("Taschentücher", "Aldi / dm", "Drogerie"),
    ("Zitronen", "Seba", "Obst & Gemüse"),
    ("Pfand abgeben", "Netto", "Sonstiges"),
    ("Karotten", "Rewe", "Obst & Gemüse"),
    ("Zwiebeln (rot/weiß)", "Aldi", "Obst & Gemüse"),
    ("Gurken", "Aldi", "Obst & Gemüse"),
    ("Tomaten", "Aldi", "Obst & Gemüse"),
    ("Milch", "Aldi", "Kühlprodukte"),
    ("Yeşil biber", "Sıla", "Obst & Gemüse"),
    ("Kırmızı biber", "Seba", "Obst & Gemüse"),
    ("Frischkäse", "Aldi", "Kühlprodukte"),
    ("Kartoffeln", "Aldi", "Obst & Gemüse"),
    ("Mercimek", "Türk. Supermarkt", "Grundnahrungsmittel"),
    ("Spüli", "dm", "Drogerie"),
    ("Sehriye", "Türk. Supermarkt", "Grundnahrungsmittel"),
    ("Wasser (Naturalis)", "Netto", "Getränke"),
    ("Beyaz Peynir Gazi", "Seba", "Kühlprodukte"),
    ("Reibekäse", "Aldi", "Kühlprodukte"),
    ("Tostbrot", "Aldi", "Brot & Backwaren"),
    ("Toilettenpapier", "dm", "Drogerie"),
    ("Islak WC-Papier", "dm", "Drogerie"),
    ("Seife", "dm", "Drogerie"),
    ("Slipeinlagen", "dm", "Drogerie"),
    ("Große Binden", "dm", "Drogerie"),
    ("Kamillentee", "dm", "Tee"),
    ("Thunfisch", "Aldi", "Konserve"),
    ("Mais", "Aldi", "Konserve"),
    ("Spaghetti", "Aldi", "Grundnahrungsmittel"),
    ("Kuskus (Makarna)", "Türk. Supermarkt", "Grundnahrungsmittel"),
    ("Tavuk", "Seba", "Fleisch"),
    ("Pirzola", "Türk. Supermarkt", "Fleisch"),
    ("Eier", "Aldi", "Kühlprodukte"),
    ("Mini Sosis", "Türk. Supermarkt", "Wurstwaren"),
    ("Türkischer Kaşar", "Seba", "Käse")
]

df = pd.DataFrame(daten, columns=["Produkt", "Einkaufsort", "Kategorie"])

# --- Anzeige der Liste ---
st.header("📋 Aktuelle Einkaufsliste")
st.dataframe(df, use_container_width=True)

# --- Platzhalter für Bon-Upload (kommt später) ---
st.header("📸 Kassenbon-Upload (in Arbeit)")
st.markdown("Hier kannst du später deinen Kassenbon hochladen – ich erkenne automatisch die Produkte und aktualisiere die Liste.")

# --- Platzhalter für Angebote, Preisvergleich, Erinnerungen ---
st.header("🔜 Geplante Funktionen")
st.markdown("- Preisvergleich & Verlauf\n- Angebots-Alarm\n- Verbrauchsbasierte Erinnerungen (z. B. Milch bald leer?)\n- Sprachsteuerung & mobile Nutzung")
