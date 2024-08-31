import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Initialize the Genius API with your access token
genius = lyricsgenius.Genius("YOUR_GENIUS_API_ACCESS_TOKEN")

# Function to fetch and display lyrics
def get_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()

    if not artist or not song:
        messagebox.showwarning("Input Error", "Please enter both artist and song name.")
        return

    try:
        song_lyrics = genius.search_song(song, artist)
        if song_lyrics:
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, song_lyrics.lyrics)
        else:
            messagebox.showinfo("No Lyrics Found", "Could not find lyrics for the song.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to clear the text fields
def clear_fields():
    artist_entry.delete(0, tk.END)
    song_entry.delete(0, tk.END)
    lyrics_text.delete(1.0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("Lyrics Extractor")

# Set window size
root.geometry("600x400")

# Artist label and entry
artist_label = tk.Label(root, text="Artist:")
artist_label.pack(pady=10)
artist_entry = tk.Entry(root, width=50)
artist_entry.pack(pady=5)

# Song label and entry
song_label = tk.Label(root, text="Song:")
song_label.pack(pady=10)
song_entry = tk.Entry(root, width=50)
song_entry.pack(pady=5)

# Fetch Lyrics Button
fetch_button = tk.Button(root, text="Get Lyrics", command=get_lyrics)
fetch_button.pack(pady=20)

# Clear Fields Button
clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack(pady=10)

# Text box to display the lyrics
lyrics_text = tk.Text(root, wrap=tk.WORD, height=10, width=60)
lyrics_text.pack(pady=10)

# Start the application
root.mainloop()
