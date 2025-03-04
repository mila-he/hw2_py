Koduülesande eesmärk on lihtsa 'veebiämbliku' koostamine vabalt valitud Eesti veebipoe lehele. 
(Ei ole lubatud kasutada 1a.ee veebipoodi), andmete lisamine andmebaasi ja selle põhjal uue veebilehe tegemine, 
kus saab päringuid teha.

Oluline on valiku juures see, et valikus oleks vähemalt 150 objekti ja 5 alamlehte. 
Kammige läbi kõik kaubad kõikidel alamlehtedel (1 kuni ...) ja looge vajadusel (kui soovite) 
JSON fail järgnevate atribuutidega: {Title: '', Price: '', Picture href: ''}. 
Kaabitsa koostamisel tuleb kasutada rekursiooni.

Palun ärge valige sellist poodi, kus valitud kategoorias oleks üle 20 alamlehe, 
sest muidu raiskab kodutööde kontrollimine liialt aega! Samal põhjusel palun ärge trükkige kaabitsemisel
saadavaid andmeid konsooli, sest 'print' käsk on suhteliselt ajamahukas.

Töö tuleb teha vabalt valitud versioonis, kas Scrapy või Beautiful Soup library-t kasutades. 
Scrapy kasutamisel peab kood käivituma ka IDE-st, mitte ainult käsurealt.
Seejärel tuleb saadud andmed automaatselt kanda andmebaasi.

Vabal valikul:
Tuleb teha kas API (nagu esimeses kodutöös) ja siis veebilehe, mis kasutab API-t 
või
Teete veebilehe, mis pöördub otse andmebaasi poole.
Veebilehel peab olema võimalik teha päringuid, et näha kõiki kaupasid, mis on kallimad kui XX eurot. 
Päringuvastus ei pea tingimata näitama pilti, piisab ka, kui on lihtsalt pildi aadress (href). 
Lehe ilusaks tegemiseks ei pea vaeva nägema, piisab funktsionaalsusest.

Tähelepanu! mõningate lehtede 'source's leidub hulgaliselt ka muud "sodi", mida ei kuvata ekraanil, 
kuid on sarnaste 'tag'idega. Neid üleliigseid, antud lehel mittekuvatavaid kaupasid ei tohi andmebaasi tekkida.
PS. Võib juhtuda, et mõningate poodide lehed ei sobi väga hästi kaabitsemiseks, 
kuna seal on kasutatud javascripti lehe kuvamiseks kaabitsemise mõistes suhteliselt ebamugaval kujul. 
Samuti võivad mõned lehed nõuda küpsiseid, ka siis on kaabitsa ehitamine veidi keerulisem (kuigi täiesti võimalik).