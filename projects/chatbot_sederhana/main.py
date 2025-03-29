def chatbot_respon(pertanyaan):
    """Chatbot sederhana yang menjawab pertanyaan berdasarkan logika if-else"""

    pertanyaan = pertanyaan.lower()

    if pertanyaan == "halo" or pertanyaan == "hai":
        return "Halo!, Bagaimana kabarmu hari ini?"
    elif pertanyaan == "siapa kamu?" or pertanyaan == "siapa kamu?" or pertanyaan == "kamu ai apa?":
        return "Aku adalah chatbot sederhana yang dibuat dengan python!"
    else:
        return "Maaf, aku belum mengerti pertanyaan itu. Coba tanyakan yang lain!"


if __name__ == "__main__":
    user_input = input("Tanyakan sesuatu pada chatbot: ")
    respon = chatbot_respon(user_input)
    print(f"chatbot: {respon}")