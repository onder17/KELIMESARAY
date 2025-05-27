from operator import index
import random
from sys import flags

question=None
t=str(True)
f=str(False)
situation= True
point=0
count=0

theQues = ["Dünyanın en büyük okyanusu:",
           "Yedi tepe üzerine kurulu şehir olarak bilinen ilimiz:",
           "Dünyanın en yüksek dağı:",
           "Dünyanın en uzun nehri:",
           "Türkiye'nin en uzun nehri:",
           "Dünyanın en büyük adası:",
           "Türkiye'nin en büyük gölü:",
           "İlk Türk devletinin adı:",
           "Fransız İhtilali'nin gerçekleştiği sene:",
           "Çanakkale Savaşı'nın gerçekleştiği yıl:",
           "Ay'a ilk ayak basan insan:",
           "Yazıyı ilk kullanan uygarlık:",
           "Türklerin Orta Asya'dan Anadolu'ya göç etmelerine verilen isim:",
           "'Mesnevi' eserine sahip tasavvufçu, şair:",
           "'Savaş ve Barış' romanının yazarı:",
           "'Mona Lisa' tablosunun ressamı:",
           "Bağımsızlık Heykeli'ne sahip olan ülke: ",
           "Piramitleriyle meşhur bir ülke:",
           "'İstiklal Marşı'nın bestecisi:",
           "Yer çekimi kanununu bulan bilim insanı:",
           "DNA'nın yapısını keşfeden bilim insanlarından biri:",
           "Ampulü icat eden bilim insanı:",
           "Kimyada Periyodik tabloyu oluşturan bilim insanı:",
           "Radyoaktiviteyi keşfeden bilim insanı:",
           "Kara delik teorisini ortaya atan bilim insanı:",
           "İlk bilgisayarı icat eden bilim insanı:",
           "Telefonu icat eden bilim insanı:",
           "Dünya Kupası'nı en çok kazanan ülke:",
           "Türkiye Süper Ligi'nde en çok şampiyon olan takım:",
           "Basketbolda NBA'de en çok şampiyon olan takım:",
           "Teniste Grand Slam turnuvalarını en çok kazanan erkek sporcu:",
           "Olimpiyat halkalarındaki renk sayısı:",
           "Futbolda en çok gol atan oyuncu:",
           "Voleybolda Dünya Şampiyonası'nı en çok kazanan ülke:",
           "Dünyanın en kalabalık ülkesi:",
           "Boynu çok uzun olan bir hayvan:",
           "Elmas kadar sert ama çok daha hafif olan bir madde:",
           "En fazla 'Oscar' ödülü kazanarak rekor kıran müzikal film:",
           "Genellikle aşkın sembolü olarak da bilinen bir çiçek:",
           "Walter White, Jesse Pinkman karakterlerinin yer aldığı ünlü dizi:",
           "'Sözleşme' anlamında Arapça kökenli söz:",
           "Bir ölçüm ve çizim aracının 'Çizelge, liste' anlamında da kullanılan adı:",
           "Harcanan çabayı,emeği karşılamaz, o kıymette değil:",
           "Sherlock Holmes hikayelerinde yer alan doktorun ismi:",
           "Basamak, safha, mertebe:",
           "Simya ilmine göre dokunduğu her maddeyi altına çevirebilen cisim:",
           "Kozmetik sektöründe de yaygın kullanılan dinamit ham maddesi:",
           "Lüks tüketim yumurtası:",
           "Bukalemun misali gizlenmek:",
           "Niyetini, düşüncesi, eğilimini anlamaya çalışmak:",
           "İşitme fonksiyonlarını test ederek ölçen aygıt:",
           "Islahatçı sözünün Fransızca kökenli eş anlamlısı:",
           "Diğer tarafa, karşı gruba geçmek:",
           "Beklenmedik, karşıt bir etki yaratmak:",
           "Tüm bedeni sarsan titreme hissi:",
           "'Argoda' birine karşı yapılan yanlış ve hatalı davranış:",
           "Çok istemek, heves duymak:",
           "'İçinden çıkılması, atlatılması güç olan bunalımlı durum:",
           "'Bireysellik' sözcüğünün Arapça kökenli eş anlamlısı:",
           "Evcimenin karşıtı, dolaşmayı çok seven:",
           "İçinde bir şey dövülüp ufalanan kap:",
           "'Termostat' ın Türkçesi:",
           "Şiddetli omuz ve sırt ağrısı:",
           "Minareleri süsleyen Ramazan ışıltıları:",
           "Bir kusurun hoş görülmesini gerektiren sebep, mazeret:",
           "Oksidasyon kızılı:",
           "Müzik parçasının farklı ritimlerle çeşitlendirilmiş hali:",
           "Sıkı sıkı, sağlı sollu kucaklamak:",
           "Üstün başarı veya hizmet karşılığı verilen onurlandırıcı ödül:",
           "Alçak gönüllülük:",
           "Normalden yüksek seviyedeki akıl cevheri:",
           "Cimri, pinti, biriktirdiğini harcamayan:",
           "İlgi ve yakınlık göstermemek:",
           "Sebze satıcısı:",
           "Vecize ve özdeyiş kelimelerinin Batı kökenli eş anlamlısı:",
           "Bilinmeyen bir yeri ortaya çıkarma:",
           "Askerlik, eğitim veya iş sürecinde birlikte olan kişiler:",
           "Beden ve kafa gücüyle ortaya konan üretim faktörü:",
           "'Aramak' fiilini 'Telaşla, heyecan içinde' anlamıyla niteleyen ikileme:",
           "Pamuk Prenses'ten Kırmızı Başlıklı Kız'a kadar birçok ünlü masalın yazarları:",
           "Adı 'Yeşil' anlamına gelen ulu şahsiyet:",
           "Volkan ağzı:",
           "Bir iş için 'üzerine konuşulmak fakat gerçekleşmemek:'",
           "Benzeri az bulunan, istisna olan:",
           "Adını, bir meyve ağacının bahar aylarında büründüğü renkten alan parlak kırmızı tonu:",
           "Aracı, mekanik ve elektronik sistemleri kullanarak belirli şartlar altında yönetebilen mekanizma:",
           "Tanrı ile evreni bir kılan öğreti, tüm tanrıcılık:",
           "Tane taneliğe prim vermeyen İtalyan pilavı:",
           "Kulaktan kulağa, dilden dile yayılan gerçekliği belirsiz olay:",
           "Oyunda kazanmak, yenmek:",
           "Elektromotor gücün veya gerilimin birimi:",
           "Gösterdiği ilgiyi kesmek:",
           "Ölmez ağaç:",
           "İki eli üstünde tepetaklak durmak:",
           "Onbinlerce devre elemanından oluşan minicik yarı iletken malzeme:",
           "Kendi ekseni etrafında hareket eden giriş-çıkış yeri:",
           "'Tekamül' veya 'Gelişme süreci' anlamındaki söz:",
           "'İlerleme, inkişaf, tekamül' anlamlarına gelen kelime:",
           "Bir düşünce veya kararı benimsemeyerek karşı çıkma:",
           "'Kargaşa içinde olan' anlamındaki Fransızca kökenli söz:",
           "'Değiştirilmiş' anlamında Fransızca kökenli bir söz:",
           "Ateşli silahla belirlenen tam hedefi vurma işi:",
           "Hafif ıslaklık, nem:",
           "Mecazen olumsuz bir durumdan veya yerden çıkıp kurtulmak:",
           "'Kriptoloji' de denen dal:",
           "Seslenmek veya yüksek sesle bildirmek:",
           "Fransızca kökenli 'değişik biçim' veya 'değişim' anlamındaki söz:",
           "'Akustik' sözünün Türkçe karşılığı:",
           "Yorgunluk veya hastalıktan gücü tükenen:",
           "Verilerin dağılımını gösteren, ortası yüksek, kenarları düşük grafik şekli:",
           "İlham almak:",
           "Sürücülere yönelik 'Hareket et, hızlan, git' anlamlarında bir direktif:",
           "Sudan sebeplerle, durup dururken sinirlenmek:",
           "El dokuması ipeği, halıları, cam ve gümüş işçiliği, havyarı, minyatür resimleri, seramik işlemeciliği ile ünlü ülke:",
           "Volkan ağzındaki durgun su birikintisi:",
           "İlhamla dolu, coşkun:",
           "Bir işi yapmadaki ustalık:",
           "Şöhretini yaymak:",
           "Tuzağa düşürmek,aldatmak:",
           "Gereksiz titizlik gösteren:",
           "Türkçe kökenli adı 'Güneşletici' olan aygıtın bilinen adı:",
           "Ispanakgillerin yüksek oranda sakkaroz içeren üyesi:",
           "'Seslendirme' nin Fransızca kökenlisi:",
           "Kronik nefes darlığı:",
           "Genellikle ince kumaşlı kadın üst giysisi:",
           "Suçluya yaptırım uygulamak:",
           "Sayıların birbiriyle işlemlerini gösteren cetvel,kerrat cetveli:",
           "Yaşanan olaydan deneyim kazanmak, tecrübe edinmek:",
           "'Ruhsal ve bedensel olarak sağlıklı yaşayın' anlamında bir iyi dilek sözü:",
           "Emek göçmeni:",
           "Yakını iyi göremeyen göz:",
           "'Yararlanma' anlamındaki Arapça kökenli söz:",
           "Arılar için de kullanılan monarşik bir ünvan:",
           "Başkenti Riga olan ülke:",
           "'Saygıdeğer' anlamında bir sözcük:",
           "Solunumu durduracak kadar çekici:",
           "'Kıvanç, iftihar' anlamında bir sözcük:",
           "Bazı sesleri kusurlu söyleyen veya tutuk konuşan kimse:",
           "Tokat'ın, adını V. Mehmet'ten alan ilçesi:",
           "Yoksulluktan düşkünleşmiş olan:",
           "Görkem, gösteriş, ihtişam, şatafat:",
           "Sınıf atlamış müstakil ev:",
           "İstanbul'un 1500 yıllık tatlı su deposu(Aynı zamanda bir sarnıç ismi):",
           "Mekke'de, Kabe'nin 20 km doğusundaki su kaynağı ve kuyusu:"











]


theAns = ["Büyük Okyanus",
          "İstanbul",
          "Everest",
          "Nil",
          "Kızılırmak",
          "Grönland",
          "Van Gölü",
          "Asya Hun Devleti",
          "1789",
          "1915",
          "Neil Armstrong",
          "Sümerler",
          "Kavimler Göçü",
          "Mevlana",
          "Tolstoy",
          "Leonardo da Vinci",
          "ABD",
          "Mısır",
          "Osman Zeki Üngör",
          "Isaac Newton",
          "James Watson",
          "Thomas Edison",
          "Mendeleyev",
          "Marie Curie",
          "Albert Einstein",
          "Charles Babbage",
          "Graham Bell",
          "Brezilya",
          "Galatasaray",
          "Boston Celtics",
          "Novak Djokovic",
          "Beş",
          "Cristiano Ronaldo",
          "Rusya",
          "Hindistan",
          "Zürafa",
          "Grafen",
          "Titanic",
          "Gül",
          "Breaking Bad",
          "Akit",
          "Cetvel",
          "Değmez",
          "Watson",
          "Etap",
          "Felsefe taşı",
          "Gliserin",
          "Havyar",
          "Kamufle olmak",
          "Nabız yoklamak",
          "Odyometre",
          "Reformist",
          "Saf değiştirmek",
          "Ters tepmek",
          "Ürperti",
          "Yamuk",
          "Can atmak",
          "Darboğaz",
          "Ferdiyet",
          "Gezenti",
          "Havan",
          "Isıdenetir",
          "Kulunç",
          "Mahya",
          "Özür",
          "Pas rengi",
          "Remiks",
          "Sarmalamak",
          "Şeref Madalyası",
          "Tevazu",
          "Üstün zeka",
          "Varyemez",
          "Yüz vermemek",
          "Zerzevatçı",
          "Aforizma",
          "Coğrafi keşif",
          "Devre arkadaşı",
          "Emek",
          "Fellik fellik",
          "Grimm Kardeşler",
          "Hızır",
          "Krater",
          "Lafta kalmak",
          "Müstesna",
          "Nar çiçeği",
          "Otopilot",
          "Panteizm",
          "Risotto",
          "Şehir efsanesi",
          "Ütmek",
          "Volt",
          "Yüz çevirmek",
          "Zeytin",
          "Amuda kalkmak",
          "Çip",
          "Döner kapı",
          "Evrim",
          "Gelişim",
          "İtiraz",
          "Kaotik",
          "Modifiye",
          "Nokta atışı",
          "Rutubet",
          "Sıyrılmak",
          "Şifre bilimi",
          "Ünlemek",
          "Varyasyon",
          "Yankılanım",
          "Bitik",
          "Çan eğrisi",
          "Esinlenmek",
          "Gazla",
          "Heyheylenmek",
          "İran",
          "Krater gölü",
          "Lirik",
          "Marifet",
          "Nam salmak",
          "Oyuna getirmek",
          "Pimpirikli",
          "Solaryum",
          "Şeker pancarı",
          "Dublaj",
          "Astım",
          "Bluz",
          "Ceza kesmek",
          "Çarpım tablosu",
          "Ders çıkarmak",
          "Esen kalın",
          "Gurbetçi",
          "Hipermetrop",
          "İstifade",
          "Kraliçe",
          "Letonya",
          "Muhterem",
          "Nefes kesici",
          "Övünç",
          "Peltek",
          "Reşadiye",
          "Sefil",
          "Şaşaa",
          "Villa",
          "Yerebatan",
          "Zemzem"

]

for numQues in range(20):
    random_index= random.randint(0,len(theQues)-1)

    #randomquestion
    takeQues=theQues[random_index]
    print(f"Soru {numQues+1}: {takeQues.upper()}")
    #correctanswer
    correct_answer = theAns[random_index]
    while True:
        response= input("--->".strip())
        if response.lower() == correct_answer.lower() or response.upper() == correct_answer.upper() or response == correct_answer:
            print(True)
            point= point+len(correct_answer)
            break
        else:
            print("False!")
            count= count+1
        if count ==5:
            print("The correct answer was:",correct_answer)
            point= point - len(correct_answer)




print("Your total point is:",point)





















            












































