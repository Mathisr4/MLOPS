from donnes_des_sous_mathis.banque import donnes_des_sous_mathis

def test_donnes_des_sous():
   result = donnes_des_sous_mathis(12,11)
   assert result == 23

def test_donne_beaucoup_des_sous():
       result = donnes_des_sous_mathis(212, 11)
       assert result == 243