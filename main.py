meme_dict = {"CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu", 'ROFL': 'tanggapan terhadap lelucon', 'SHEESH': 'sedikit ketidak setujuan',
            'CREEPY':  'menakutkan, tidak menyenangkan'}
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('mohon maaf kata kata tidak tersedia')
