przedstaw = ('Dzień dobry, nazywam się Michał Podwysocki i dzwonię w imieniu operatora \n telekomunikacyjnego Tele tombola.\n Proszę o połączenie z osobą odpowiedzialną za usługi telekomunikacyjne.\n Z kim będę rozmawiać?')
print (przedstaw)

zgoda = input("Czy rozmówca się zgodził? ").lower()
if zgoda == 't':
    print('Dziękuje bardzo!')
    przedstaw2 =('\n Dzień dobry nazywam się Michał Podwysocki i dzwonię w imieniu \n operatora telekomunikacyjnego Teletombola')
    print (przedstaw2)
    pytanie = input("Czy korzystają już może Państwo z usług Tele tomboli? ").lower()
    if pytanie =='t':
        print('Czy są Państwo zadowoleni ze świadczonych usług? Czy może potrzebny jest kontakt naszego opiekuna? ')
        zadowolony = input('t').lower()
        if zadowolony == 't':
            print('Bardzo się cieszę. Dziękuje za opinię. Życzę miłego dnia!!!')
        elif zadowolony == 'n':
            print('A...rozumiem...Pozwoli Pan/i że niezwłocznie przekażę tę informację \n do Państwa opiekuna.\n - potwierdzić dane osoby kontaktowej \n- zapisać imię,nazwisko,stanowisko.\n - zapisać numer telefonu kontaktowego\n\n\n Dziękuje za informację życzę miłego dnia ')
    elif pytanie == 'n':
            print('Proponujemy Państwu bezpłatne spotkanie z naszym specjalistą w celu \n sprawdzenia możliwości obniżenia dotychczasowych kosztów na usługi \n telekomunikacyjne.\n\n Na kiedy mogę umówić wizytę? ')
            zgoda_na_spotkanie = input ('t').lower()
            if zgoda_na_spotkanie == 't':
                print('Proszę podać datę, godzinę i miejsce spotkania? \n A jaki operator świadczy Państwu usługi teraz? ')
            elif zgoda_na_spotkanie == 'n':
                    print('(a) jeśli klient chce kontaktu telefonicznego:\n - zapisanie numeru telefonu \n - potwierdzenie danych osobowych osoby kontaktowej \n (b) jeśli klient chce tylko informacji mailowej: \n skłonić do zgody na uprzedni kontakt telefoniczny specjalisty argumentem: \n\n\n POZWOLI PAN/I , ŻE PRZEDTEM NASZ SPECJALISTA ZADZWONI W CELU POZNANIA PAŃSTWA WYMAGAŃ \n\n BARDZO DZIĘKUJE ZA ROZMOWĘ. ŻYCZĘ MIŁĘGO DNIA!!! ')
elif zgoda == 'n':
    print('Dziękuje za rozmowę. Życzę miłego dnia!')
   





