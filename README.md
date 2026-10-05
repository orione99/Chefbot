# 👨‍🍳 ChefBot AI - Assistente Intelligente per Riconoscimento Cibo e Ricerca per Umore

ChefBot AI è un sistema di Intelligenza Artificiale multimodale progettato per identificare piatti a partire da fotografie e raccomandare alimenti in base all'umore o alle preferenze espresse dall'utente via testo.

Il sistema combina **Computer Vision** (Transfer Learning con MobileNetV2) e **Natural Language Processing** (Sentence Transformers) integrandosi con un database di conoscenza in formato JSON.

---

## 📌 Architettura del Sistema

Il progetto si compone di due moduli principali coordinati da una pipeline centrale:

1. **Riconoscimento Visivo (Computer Vision)**:
   * **Architettura Base**: `MobileNetV2` pre-addestrata su ImageNet.
   * **Tecnica**: Transfer Learning / Feature Extraction (pesi del backbone congelati).
   * **Data Augmentation**: Applicata nella fase di training (`RandomResizedCrop`, `RandomHorizontalFlip`, `RandomRotation`, `ColorJitter`).
   * **Early Stopping**: Monitora la `Validation Loss` e salva automaticamente i pesi ottimali nel file `best_chefbot_model.pt`.

2. **Ricerca Semantica per Umore (NLP)**:
   * **Modello**: `paraphrase-multilingual-MiniLM-L12-v2` (Sentence Transformers).
   * **Algoritmo**: Generazione di vettori normalizzati (L2) e calcolo della **Cosine Similarity**.
   * **Risultato**: Restituzione dei **Top-3 piatti** più coerenti con il desiderio o stato d'animo espresso dall'utente.

3. **Database di Conoscenza (`database.json`)**:
   * Contiene i metadati di 15 piatti (ingredienti, valori nutrizionali calorici e macro, e descrizioni testuali calibrate).

---

## 📁 Struttura del Progetto

```text
Chefbot/
├── database.json             # Database JSON con metadati nutrizionali e descrizioni
├── create_dataset_image.py   # Script opzionale per il download/download automatizzato dei dati
├── app.ipynb                 # Notebook Jupyter principale con il codice del progetto
├── requirements.txt          # Dipendenze del progetto
└── README.md                 # Documentazione del progetto