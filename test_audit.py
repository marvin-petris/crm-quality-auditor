from audit import age_est_valide, email_est_valide, telephone_est_valide

def test_age_est_valide():
    assert age_est_valide("25") == True
    assert age_est_valide("150") == False
    assert age_est_valide("abc") == False
    assert age_est_valide("0") == False

def test_email_est_valide():
    assert email_est_valide("jean.dupont@example.com") == True
    assert email_est_valide("jean.dupontexample.com") == False
    assert email_est_valide("@example.com") == False

def test_telephone_est_valide():
    assert telephone_est_valide("0639980000") == True
    assert telephone_est_valide("0626") == False
    assert telephone_est_valide("1234567890") == False