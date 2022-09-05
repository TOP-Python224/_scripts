from pprint import pprint

people = [
	{
		'name': "Libby Rosario",
		'age': 50,
		'email': "mollis.integer@ya.ru",
		'phone': "+7-908-818-2166",
		'langs': "KZ FR JP"
	},
	{
		'name': "Bevis Roberts",
		'age': 58,
		'email': "sem.pellentesque@mail.ru",
		'phone': "+7-922-145-0123",
		'langs': "EN KZ"
	},
	{
		'name': "Oscar Myers",
		'age': 44,
		'email': "mauris.rhoncus.id@e1.ru",
		'phone': "+7-956-608-1558",
		'langs': "EN RU"
	},
	{
		'name': "Brock Russo",
		'age': 24,
		'email': "dui.lectus.rutrum@yandex.ru",
		'phone': "+7-964-262-1021",
		'langs': "JP FR SP"
	},
	{
		'name': "Byron Marquez",
		'age': 65,
		'email': "vivamus@ya.ru",
		'phone': "+7-998-428-4675",
		'langs': "SP FR KZ"
	},
	{
		'name': "Joy Reyes",
		'age': 31,
		'email': "tempus.mauris@ya.ru",
		'phone': "+7-944-303-8644",
		'langs': "EN JP CN RU"
	},
	{
		'name': "Tyrone Heath",
		'age': 43,
		'email': "mauris.vel.turpis@yandex.ru",
		'phone': "+7-983-206-9541",
		'langs': "KZ RU FR"
	},
	{
		'name': "Mikayla Donaldson",
		'age': 39,
		'email': "scelerisque.scelerisque@yandex.ru",
		'phone': "+7-988-834-4126",
		'langs': "CN JP"
	},
	{
		'name': "Raven Pierce",
		'age': 59,
		'email': "libero.at@mail.ru",
		'phone': "+7-913-453-8819",
		'langs': "JP KZ FR RU"
	},
	{
		'name': "Macon Murray",
		'age': 30,
		'email': "montes.nascetur@e1.ru",
		'phone': "+7-989-834-0564",
		'langs': "FR"
	},
	{
		'name': "Brent Munoz",
		'age': 35,
		'email': "mi@ya.ru",
		'phone': "+7-977-628-8253",
		'langs': "FR KZ EN"
	},
	{
		'name': "Holmes Summers",
		'age': 64,
		'email': "gravida.molestie@e1.ru",
		'phone': "+7-989-117-6926",
		'langs': "RU"
	},
	{
		'name': "Bernard Morrow",
		'age': 40,
		'email': "aliquet@e1.ru",
		'phone': "+7-955-794-9882",
		'langs': "SP KZ FR"
	},
	{
		'name': "Yetta Good",
		'age': 57,
		'email': "purus.accumsan.interdum@yandex.ru",
		'phone': "+7-955-827-8189",
		'langs': "KZ SP JP"
	},
	{
		'name': "Rinah Massey",
		'age': 58,
		'email': "in@mail.ru",
		'phone': "+7-936-781-0431",
		'langs': "SP KZ"
	},
	{
		'name': "Herman Thornton",
		'age': 37,
		'email': "quis.accumsan@yandex.ru",
		'phone': "+7-915-662-9326",
		'langs': "SP"
	},
	{
		'name': "Hashim Hunt",
		'age': 53,
		'email': "tempor.lorem.eget@mail.ru",
		'phone': "+7-981-319-4018",
		'langs': "SP FR JP"
	},
	{
		'name': "Keegan Lane",
		'age': 21,
		'email': "nonummy.ipsum@ya.ru",
		'phone': "+7-984-297-9026",
		'langs': "SP FR JP"
	},
	{
		'name': "Justin Solomon",
		'age': 20,
		'email': "integer@ya.ru",
		'phone': "+7-959-524-5991",
		'langs': "RU"
	},
	{
		'name': "Sylvia Rodgers",
		'age': 43,
		'email': "magna.a@mail.ru",
		'phone': "+7-993-743-5858",
		'langs': "EN JP SP RU"
	},
	{
		'name': "Victor Manning",
		'age': 36,
		'email': "lacinia@mail.ru",
		'phone': "+7-995-346-1113",
		'langs': "SP FR"
	},
	{
		'name': "April Hines",
		'age': 54,
		'email': "lacus.nulla.tincidunt@mail.ru",
		'phone': "+7-992-232-7659",
		'langs': "KZ SP"
	},
	{
		'name': "Whilemina Hodge",
		'age': 19,
		'email': "non.enim@ya.ru",
		'phone': "+7-964-464-9158",
		'langs': "SP"
	},
	{
		'name': "Adam Schmidt",
		'age': 58,
		'email': "euismod.in@mail.ru",
		'phone': "+7-913-885-8492",
		'langs': "RU FR KZ"
	},
	{
		'name': "Nyssa Gutierrez",
		'age': 41,
		'email': "aliquet.odio.etiam@ya.ru",
		'phone': "+7-977-355-3361",
		'langs': "SP EN FR"
	},
	{
		'name': "Gregory Jordan",
		'age': 37,
		'email': "dui.quis.accumsan@yandex.ru",
		'phone': "+7-975-454-6430",
		'langs': "JP FR"
	},
	{
		'name': "Lilah William",
		'age': 23,
		'email': "nunc.ullamcorper@ya.ru",
		'phone': "+7-916-328-3212",
		'langs': "KZ JP"
	},
	{
		'name': "Alexandra Jacobson",
		'age': 46,
		'email': "iaculis.lacus@yandex.ru",
		'phone': "+7-932-974-3661",
		'langs': "JP FR"
	},
	{
		'name': "Carl Rodgers",
		'age': 27,
		'email': "sit.amet@yandex.ru",
		'phone': "+7-904-467-2435",
		'langs': "SP KZ JP EN"
	},
	{
		'name': "Melodie Salas",
		'age': 48,
		'email': "enim.nisl.elementum@e1.ru",
		'phone': "+7-967-518-0122",
		'langs': "FR RU EN"
	},
	{
		'name': "Erich Singleton",
		'age': 35,
		'email': "ultrices.posuere.cubilia@yandex.ru",
		'phone': "+7-952-763-1686",
		'langs': "EN CN"
	},
	{
		'name': "David Gates",
		'age': 43,
		'email': "accumsan@ya.ru",
		'phone': "+7-924-556-7584",
		'langs': "SP KZ RU"
	},
	{
		'name': "Giacomo Cannon",
		'age': 46,
		'email': "a.dui@e1.ru",
		'phone': "+7-943-788-4148",
		'langs': "FR SP CN"
	},
	{
		'name': "August Vaughan",
		'age': 52,
		'email': "sapien@e1.ru",
		'phone': "+7-965-505-0357",
		'langs': "KZ CN"
	},
	{
		'name': "Brody Carpenter",
		'age': 28,
		'email': "cubilia.curae@yandex.ru",
		'phone': "+7-927-450-2711",
		'langs': "RU FR EN"
	},
	{
		'name': "Melinda Jennings",
		'age': 23,
		'email': "adipiscing@ya.ru",
		'phone': "+7-933-672-6444",
		'langs': "JP KZ"
	},
	{
		'name': "Driscoll Horton",
		'age': 51,
		'email': "quisque.ornare@ya.ru",
		'phone': "+7-938-978-7489",
		'langs': "RU SP CN"
	},
	{
		'name': "Kylee Moreno",
		'age': 44,
		'email': "mauris@e1.ru",
		'phone': "+7-916-701-0158",
		'langs': "FR JP EN KZ"
	},
	{
		'name': "Amber Bowman",
		'age': 33,
		'email': "a.tortor@e1.ru",
		'phone': "+7-942-269-3411",
		'langs': "EN KZ SP"
	},
	{
		'name': "Barbara Wynn",
		'age': 35,
		'email': "dui@mail.ru",
		'phone': "+7-922-751-8113",
		'langs': "SP"
	},
	{
		'name': "Kenyon Castillo",
		'age': 40,
		'email': "nec@e1.ru",
		'phone': "+7-967-812-3596",
		'langs': "FR KZ SP"
	},
	{
		'name': "Nita Stone",
		'age': 64,
		'email': "vitae.erat@mail.ru",
		'phone': "+7-977-278-9815",
		'langs': "SP CN"
	},
	{
		'name': "Dieter Potter",
		'age': 54,
		'email': "adipiscing.non@yandex.ru",
		'phone': "+7-954-424-9218",
		'langs': "JP CN RU"
	},
	{
		'name': "Quon Gilbert",
		'age': 28,
		'email': "sodales.mauris.blandit@e1.ru",
		'phone': "+7-946-761-3453",
		'langs': "SP RU"
	},
	{
		'name': "Xaviera Townsend",
		'age': 63,
		'email': "convallis.ligula@e1.ru",
		'phone': "+7-932-117-2406",
		'langs': "CN KZ"
	},
	{
		'name': "Sade Sherman",
		'age': 22,
		'email': "sagittis@e1.ru",
		'phone': "+7-985-143-4384",
		'langs': "KZ CN EN"
	},
	{
		'name': "Leigh Baldwin",
		'age': 34,
		'email': "cum.sociis@yandex.ru",
		'phone': "+7-917-428-6371",
		'langs': "EN"
	},
	{
		'name': "Ezra Peck",
		'age': 57,
		'email': "est.congue.a@mail.ru",
		'phone': "+7-934-166-8437",
		'langs': "EN"
	},
	{
		'name': "Jasmine Wynn",
		'age': 60,
		'email': "semper.cursus.integer@yandex.ru",
		'phone': "+7-947-313-6836",
		'langs': "CN SP"
	},
	{
		'name': "Nina Wiley",
		'age': 49,
		'email': "nam.interdum.enim@mail.ru",
		'phone': "+7-953-815-4583",
		'langs': "SP RU"
	},
	{
		'name': "Plato Clarke",
		'age': 47,
		'email': "ligula.eu.enim@mail.ru",
		'phone': "+7-956-464-8253",
		'langs': "EN JP RU"
	},
	{
		'name': "Jarrod Mccullough",
		'age': 31,
		'email': "vel@e1.ru",
		'phone': "+7-972-582-5778",
		'langs': "EN"
	},
	{
		'name': "Rafael Ruiz",
		'age': 19,
		'email': "massa.mauris@yandex.ru",
		'phone': "+7-983-713-2024",
		'langs': "CN SP FR"
	},
	{
		'name': "Lucy Bradshaw",
		'age': 18,
		'email': "eget@e1.ru",
		'phone': "+7-937-995-5657",
		'langs': "CN RU KZ"
	},
	{
		'name': "Brenna Morin",
		'age': 22,
		'email': "nostra.per@ya.ru",
		'phone': "+7-979-221-6652",
		'langs': "CN KZ JP FR"
	},
	{
		'name': "Madonna Mason",
		'age': 48,
		'email': "sed.dictum@yandex.ru",
		'phone': "+7-924-131-8640",
		'langs': "EN SP"
	},
	{
		'name': "Uriah Juarez",
		'age': 54,
		'email': "massa@e1.ru",
		'phone': "+7-919-783-3351",
		'langs': "CN EN KZ RU"
	},
	{
		'name': "Jakeem Macdonald",
		'age': 37,
		'email': "mollis.integer@mail.ru",
		'phone': "+7-956-858-3143",
		'langs': "RU FR CN JP"
	},
	{
		'name': "Dexter Reilly",
		'age': 26,
		'email': "ac.urna.ut@ya.ru",
		'phone': "+7-964-924-4532",
		'langs': "CN JP"
	},
	{
		'name': "Pandora Nunez",
		'age': 43,
		'email': "scelerisque@mail.ru",
		'phone': "+7-949-410-9556",
		'langs': "FR"
	},
	{
		'name': "Prescott Lee",
		'age': 38,
		'email': "congue.in@yandex.ru",
		'phone': "+7-958-985-2365",
		'langs': "EN JP SP"
	},
	{
		'name': "Jasper Byrd",
		'age': 61,
		'email': "proin.velit@e1.ru",
		'phone': "+7-942-647-4865",
		'langs': "KZ FR EN SP"
	},
	{
		'name': "Myra Mcleod",
		'age': 51,
		'email': "eget.metus.eu@ya.ru",
		'phone': "+7-994-482-0860",
		'langs': "RU FR EN"
	},
	{
		'name': "Lara Clements",
		'age': 39,
		'email': "nec@yandex.ru",
		'phone': "+7-972-290-4381",
		'langs': "JP KZ"
	},
	{
		'name': "Jorden Britt",
		'age': 48,
		'email': "mauris.molestie@yandex.ru",
		'phone': "+7-935-420-1548",
		'langs': "EN"
	},
	{
		'name': "Rachel Figueroa",
		'age': 22,
		'email': "ut.dolor@e1.ru",
		'phone': "+7-984-714-6775",
		'langs': "JP SP KZ"
	},
	{
		'name': "Demetrius Goff",
		'age': 30,
		'email': "ligula@yandex.ru",
		'phone': "+7-997-495-6349",
		'langs': "SP FR JP"
	},
	{
		'name': "Troy Pate",
		'age': 63,
		'email': "amet.nulla@yandex.ru",
		'phone': "+7-907-822-0718",
		'langs': "SP"
	},
	{
		'name': "TaShya Klein",
		'age': 52,
		'email': "a.tortor@ya.ru",
		'phone': "+7-953-272-8794",
		'langs': "EN RU"
	},
	{
		'name': "Kennan Shepard",
		'age': 26,
		'email': "accumsan.sed@yandex.ru",
		'phone': "+7-979-358-0346",
		'langs': "RU"
	},
	{
		'name': "Elton Irwin",
		'age': 55,
		'email': "cum.sociis.natoque@mail.ru",
		'phone': "+7-945-785-6833",
		'langs': "RU CN EN"
	},
	{
		'name': "Odysseus Perry",
		'age': 42,
		'email': "sem.nulla.interdum@e1.ru",
		'phone': "+7-943-536-8654",
		'langs': "RU"
	},
	{
		'name': "Gabriel Goodwin",
		'age': 38,
		'email': "mi.duis@e1.ru",
		'phone': "+7-944-245-2836",
		'langs': "EN"
	},
	{
		'name': "Ima Jacobson",
		'age': 25,
		'email': "ultrices.a@mail.ru",
		'phone': "+7-957-667-5343",
		'langs': "CN SP"
	},
	{
		'name': "Roanna Kerr",
		'age': 53,
		'email': "in.magna@mail.ru",
		'phone': "+7-924-311-3611",
		'langs': "EN"
	},
	{
		'name': "Bryar Chan",
		'age': 47,
		'email': "cras.eu@mail.ru",
		'phone': "+7-904-907-2728",
		'langs': "JP"
	},
	{
		'name': "Gavin Hughes",
		'age': 37,
		'email': "elementum@e1.ru",
		'phone': "+7-966-925-3747",
		'langs': "CN"
	},
	{
		'name': "Ignatius Caldwell",
		'age': 27,
		'email': "aenean.euismod@e1.ru",
		'phone': "+7-931-223-7881",
		'langs': "RU JP KZ"
	},
	{
		'name': "Moana Hernandez",
		'age': 20,
		'email': "at.velit.cras@e1.ru",
		'phone': "+7-932-996-4061",
		'langs': "CN FR"
	},
	{
		'name': "Paula Olson",
		'age': 22,
		'email': "fermentum.metus@ya.ru",
		'phone': "+7-984-416-5406",
		'langs': "CN"
	},
	{
		'name': "Rylee Hendrix",
		'age': 40,
		'email': "sit.amet.luctus@mail.ru",
		'phone': "+7-945-704-3173",
		'langs': "SP"
	},
	{
		'name': "Gretchen Rodriguez",
		'age': 47,
		'email': "egestas.sed@mail.ru",
		'phone': "+7-946-085-5731",
		'langs': "RU EN CN"
	},
	{
		'name': "Devin Rhodes",
		'age': 51,
		'email': "dolor.quisque@mail.ru",
		'phone': "+7-975-548-4875",
		'langs': "EN KZ FR RU"
	},
	{
		'name': "Tara Russo",
		'age': 48,
		'email': "ornare.placerat@mail.ru",
		'phone': "+7-914-520-1800",
		'langs': "JP SP"
	},
	{
		'name': "Hadley Houston",
		'age': 34,
		'email': "integer.tincidunt.aliquam@yandex.ru",
		'phone': "+7-957-919-8515",
		'langs': "RU KZ FR"
	},
	{
		'name': "Ethan Medina",
		'age': 56,
		'email': "ullamcorper.eu@e1.ru",
		'phone': "+7-938-971-5513",
		'langs': "FR CN EN"
	},
	{
		'name': "Forrest Porter",
		'age': 61,
		'email': "aliquet@yandex.ru",
		'phone': "+7-976-901-2743",
		'langs': "SP KZ"
	},
	{
		'name': "William Hayes",
		'age': 32,
		'email': "ut.nulla@mail.ru",
		'phone': "+7-937-047-1165",
		'langs': "FR JP CN"
	},
	{
		'name': "Desiree Bender",
		'age': 36,
		'email': "montes.nascetur.ridiculus@ya.ru",
		'phone': "+7-948-224-5143",
		'langs': "RU FR JP SP"
	},
	{
		'name': "Fay Shaffer",
		'age': 28,
		'email': "proin@ya.ru",
		'phone': "+7-987-274-1755",
		'langs': "EN SP"
	},
	{
		'name': "Tanek Peters",
		'age': 65,
		'email': "nibh@e1.ru",
		'phone': "+7-965-885-3338",
		'langs': "CN EN SP"
	},
	{
		'name': "Brennan Huber",
		'age': 64,
		'email': "nec@mail.ru",
		'phone': "+7-909-833-9167",
		'langs': "EN"
	},
	{
		'name': "Bert Booker",
		'age': 27,
		'email': "justo@e1.ru",
		'phone': "+7-961-918-0722",
		'langs': "JP EN FR RU"
	},
	{
		'name': "Thomas Dillon",
		'age': 27,
		'email': "pharetra.nibh@ya.ru",
		'phone': "+7-937-885-6295",
		'langs': "SP KZ EN JP"
	},
	{
		'name': "Teagan Reynolds",
		'age': 53,
		'email': "amet@yandex.ru",
		'phone': "+7-942-348-1806",
		'langs': "CN EN"
	},
	{
		'name': "Wang Rivas",
		'age': 58,
		'email': "pharetra.ut@yandex.ru",
		'phone': "+7-956-365-3724",
		'langs': "JP CN RU SP"
	},
	{
		'name': "Vivien William",
		'age': 45,
		'email': "consectetuer.rhoncus@e1.ru",
		'phone': "+7-968-863-7588",
		'langs': "CN JP SP"
	},
	{
		'name': "Illana Winters",
		'age': 51,
		'email': "tempor.bibendum@ya.ru",
		'phone': "+7-942-573-9446",
		'langs': "JP SP"
	},
	{
		'name': "Robert Olsen",
		'age': 22,
		'email': "faucibus.orci@ya.ru",
		'phone': "+7-932-374-5511",
		'langs': "KZ SP"
	},
	{
		'name': "Lila Webb",
		'age': 34,
		'email': "arcu.imperdiet.ullamcorper@yandex.ru",
		'phone': "+7-993-118-5795",
		'langs': "SP KZ RU CN"
	},
	{
		'name': "Macon Carney",
		'age': 63,
		'email': "cursus@mail.ru",
		'phone': "+7-957-312-0003",
		'langs': "JP SP"
	},
	{
		'name': "Prescott Cotton",
		'age': 56,
		'email': "imperdiet.non@yandex.ru",
		'phone': "+7-917-642-8787",
		'langs': "FR SP CN"
	},
	{
		'name': "Vielka Mckenzie",
		'age': 22,
		'email': "erat.semper.rutrum@mail.ru",
		'phone': "+7-984-122-6424",
		'langs': "FR EN JP CN"
	},
	{
		'name': "Stuart Ford",
		'age': 31,
		'email': "vitae.mauris@e1.ru",
		'phone': "+7-962-848-1182",
		'langs': "RU FR"
	},
	{
		'name': "Leonard Blackwell",
		'age': 63,
		'email': "diam@mail.ru",
		'phone': "+7-963-337-7613",
		'langs': "CN JP SP EN"
	},
	{
		'name': "Caesar Salas",
		'age': 64,
		'email': "nulla.vulputate@mail.ru",
		'phone': "+7-977-415-3405",
		'langs': "JP"
	},
	{
		'name': "Zephania Barron",
		'age': 52,
		'email': "mauris.elit@e1.ru",
		'phone': "+7-907-224-6644",
		'langs': "FR"
	},
	{
		'name': "Dara Navarro",
		'age': 41,
		'email': "turpis.egestas@mail.ru",
		'phone': "+7-988-535-5547",
		'langs': "RU JP"
	},
	{
		'name': "Vernon Ramos",
		'age': 43,
		'email': "nunc@ya.ru",
		'phone': "+7-963-518-5077",
		'langs': "JP CN"
	},
	{
		'name': "Kelsie Blanchard",
		'age': 22,
		'email': "nisi.sem@yandex.ru",
		'phone': "+7-924-536-1626",
		'langs': "RU CN SP"
	},
	{
		'name': "Cody Ortiz",
		'age': 35,
		'email': "nec@e1.ru",
		'phone': "+7-956-034-6847",
		'langs': "EN FR JP"
	},
	{
		'name': "Samson Davenport",
		'age': 37,
		'email': "vivamus.nisi@yandex.ru",
		'phone': "+7-986-767-9360",
		'langs': "SP"
	},
	{
		'name': "Allegra Mcpherson",
		'age': 35,
		'email': "sit@e1.ru",
		'phone': "+7-917-853-0726",
		'langs': "EN JP FR"
	},
	{
		'name': "Xavier Cooke",
		'age': 43,
		'email': "vel.quam@ya.ru",
		'phone': "+7-944-412-7887",
		'langs': "FR KZ RU"
	},
	{
		'name': "Quemby White",
		'age': 22,
		'email': "nullam.enim.sed@yandex.ru",
		'phone': "+7-976-217-7457",
		'langs': "KZ SP JP EN"
	},
	{
		'name': "Stella Tyler",
		'age': 30,
		'email': "enim.nunc.ut@mail.ru",
		'phone': "+7-972-628-0262",
		'langs': "CN SP JP RU"
	},
	{
		'name': "Scott Hayes",
		'age': 22,
		'email': "iaculis@ya.ru",
		'phone': "+7-927-588-1205",
		'langs': "CN JP KZ"
	},
	{
		'name': "Zahir Keith",
		'age': 19,
		'email': "nec.euismod.in@e1.ru",
		'phone': "+7-921-606-3743",
		'langs': "SP JP CN RU"
	},
	{
		'name': "Anastasia Jennings",
		'age': 33,
		'email': "ipsum.primis.in@mail.ru",
		'phone': "+7-903-779-2584",
		'langs': "CN"
	},
	{
		'name': "Wendy Guthrie",
		'age': 19,
		'email': "luctus@yandex.ru",
		'phone': "+7-923-630-6880",
		'langs': "KZ"
	},
	{
		'name': "Quentin Ryan",
		'age': 38,
		'email': "tellus.phasellus.elit@mail.ru",
		'phone': "+7-925-196-8716",
		'langs': "KZ RU JP"
	},
	{
		'name': "Judith Thompson",
		'age': 34,
		'email': "penatibus@mail.ru",
		'phone': "+7-942-873-5247",
		'langs': "JP FR KZ CN"
	},
	{
		'name': "Vaughan Carson",
		'age': 63,
		'email': "nunc.ac@e1.ru",
		'phone': "+7-976-668-6679",
		'langs': "RU"
	},
	{
		'name': "Yvette Ellison",
		'age': 21,
		'email': "augue.malesuada@ya.ru",
		'phone': "+7-944-866-5830",
		'langs': "FR"
	},
	{
		'name': "Rhoda Macias",
		'age': 23,
		'email': "massa.integer@e1.ru",
		'phone': "+7-979-037-7845",
		'langs': "JP CN"
	},
	{
		'name': "Beverly Bernard",
		'age': 53,
		'email': "mollis@ya.ru",
		'phone': "+7-999-836-4555",
		'langs': "SP CN EN"
	},
	{
		'name': "Preston Aguilar",
		'age': 38,
		'email': "lobortis.mauris@e1.ru",
		'phone': "+7-957-518-8243",
		'langs': "EN JP SP RU"
	},
	{
		'name': "Ronan Singleton",
		'age': 30,
		'email': "ridiculus@ya.ru",
		'phone': "+7-947-140-2612",
		'langs': "KZ EN CN"
	},
	{
		'name': "Harlan Leon",
		'age': 54,
		'email': "facilisis@e1.ru",
		'phone': "+7-907-291-1069",
		'langs': "CN EN"
	},
	{
		'name': "Drew Armstrong",
		'age': 38,
		'email': "sodales@ya.ru",
		'phone': "+7-941-647-4536",
		'langs': "KZ EN JP"
	},
	{
		'name': "Sawyer Crosby",
		'age': 27,
		'email': "cursus@e1.ru",
		'phone': "+7-908-656-1727",
		'langs': "CN"
	},
	{
		'name': "Hannah Faulkner",
		'age': 31,
		'email': "felis@mail.ru",
		'phone': "+7-912-286-5822",
		'langs': "SP RU JP"
	},
	{
		'name': "Alden Lane",
		'age': 18,
		'email': "neque.in.ornare@mail.ru",
		'phone': "+7-953-726-5184",
		'langs': "CN FR EN"
	},
	{
		'name': "Sydney Patel",
		'age': 40,
		'email': "vitae.mauris.sit@mail.ru",
		'phone': "+7-956-395-0430",
		'langs': "EN CN"
	},
	{
		'name': "Bevis Brady",
		'age': 23,
		'email': "a.enim@ya.ru",
		'phone': "+7-997-464-3618",
		'langs': "KZ"
	},
	{
		'name': "Alexis Banks",
		'age': 39,
		'email': "lacus.pede@ya.ru",
		'phone': "+7-933-427-5629",
		'langs': "FR SP"
	},
	{
		'name': "Colby Yates",
		'age': 64,
		'email': "nisi.cum@mail.ru",
		'phone': "+7-905-429-7107",
		'langs': "JP KZ"
	},
	{
		'name': "Clinton Clayton",
		'age': 59,
		'email': "nunc.ac.mattis@yandex.ru",
		'phone': "+7-947-669-5333",
		'langs': "SP"
	},
	{
		'name': "Ivor Sykes",
		'age': 46,
		'email': "nec@e1.ru",
		'phone': "+7-987-637-5368",
		'langs': "CN EN"
	},
	{
		'name': "Jane Griffith",
		'age': 44,
		'email': "dui.fusce@yandex.ru",
		'phone': "+7-943-111-3507",
		'langs': "KZ RU FR JP"
	},
	{
		'name': "Channing Hobbs",
		'age': 52,
		'email': "est.tempor.bibendum@ya.ru",
		'phone': "+7-928-356-6828",
		'langs': "JP CN EN"
	},
	{
		'name': "Imani Miranda",
		'age': 51,
		'email': "proin.vel@mail.ru",
		'phone': "+7-916-273-8259",
		'langs': "JP RU SP CN"
	},
	{
		'name': "Walker Fitzgerald",
		'age': 36,
		'email': "ut@ya.ru",
		'phone': "+7-913-801-3281",
		'langs': "SP RU"
	},
	{
		'name': "Quentin Simpson",
		'age': 46,
		'email': "sed.auctor@ya.ru",
		'phone': "+7-962-931-1164",
		'langs': "KZ EN SP FR"
	},
	{
		'name': "Ashton Whitfield",
		'age': 25,
		'email': "molestie.dapibus@yandex.ru",
		'phone': "+7-919-481-5218",
		'langs': "EN SP"
	},
	{
		'name': "Whitney Washington",
		'age': 53,
		'email': "orci@mail.ru",
		'phone': "+7-904-584-3771",
		'langs': "EN"
	},
	{
		'name': "Venus Spears",
		'age': 28,
		'email': "ipsum.primis@ya.ru",
		'phone': "+7-952-565-3653",
		'langs': "RU KZ"
	},
	{
		'name': "Logan Clayton",
		'age': 36,
		'email': "sapien.molestie@ya.ru",
		'phone': "+7-965-750-0630",
		'langs': "EN FR JP"
	},
	{
		'name': "Boris Reyes",
		'age': 62,
		'email': "duis.risus.odio@e1.ru",
		'phone': "+7-917-823-1772",
		'langs': "RU"
	},
	{
		'name': "Tyrone Lara",
		'age': 18,
		'email': "ut.mi.duis@ya.ru",
		'phone': "+7-949-613-8653",
		'langs': "FR EN SP"
	},
	{
		'name': "Tiger Nieves",
		'age': 22,
		'email': "sed@ya.ru",
		'phone': "+7-952-645-7407",
		'langs': "FR JP"
	},
	{
		'name': "Ginger Middleton",
		'age': 42,
		'email': "magna@ya.ru",
		'phone': "+7-963-867-4784",
		'langs': "SP CN"
	},
	{
		'name': "Jacob Pope",
		'age': 28,
		'email': "duis.dignissim@yandex.ru",
		'phone': "+7-981-844-9266",
		'langs': "CN JP"
	},
	{
		'name': "Norman Noble",
		'age': 39,
		'email': "at.arcu.vestibulum@yandex.ru",
		'phone': "+7-964-308-6121",
		'langs': "KZ CN"
	},
	{
		'name': "Ezra Washington",
		'age': 23,
		'email': "pharetra.ut@e1.ru",
		'phone': "+7-915-205-2822",
		'langs': "EN CN RU KZ"
	},
	{
		'name': "Sigourney Hoffman",
		'age': 46,
		'email': "congue@e1.ru",
		'phone': "+7-928-819-7477",
		'langs': "SP KZ JP"
	},
	{
		'name': "Nehru Mann",
		'age': 47,
		'email': "et.eros.proin@e1.ru",
		'phone': "+7-925-483-6215",
		'langs': "KZ SP JP"
	},
	{
		'name': "Buffy Ramirez",
		'age': 62,
		'email': "semper.erat@yandex.ru",
		'phone': "+7-955-913-8759",
		'langs': "RU FR"
	},
	{
		'name': "Chaney Bishop",
		'age': 22,
		'email': "tristique@ya.ru",
		'phone': "+7-964-321-0158",
		'langs': "CN JP"
	},
	{
		'name': "Leonard Camacho",
		'age': 52,
		'email': "purus.mauris@e1.ru",
		'phone': "+7-957-254-2045",
		'langs': "FR SP"
	},
	{
		'name': "Suki Wolfe",
		'age': 51,
		'email': "enim.gravida@mail.ru",
		'phone': "+7-968-867-1348",
		'langs': "EN FR"
	},
	{
		'name': "Nicole Hurst",
		'age': 31,
		'email': "turpis.nec.mauris@yandex.ru",
		'phone': "+7-935-764-6226",
		'langs': "FR SP"
	},
	{
		'name': "Sonia Nolan",
		'age': 27,
		'email': "montes.nascetur.ridiculus@ya.ru",
		'phone': "+7-918-565-0560",
		'langs': "CN EN RU"
	},
	{
		'name': "Hayfa Moreno",
		'age': 21,
		'email': "morbi.sit.amet@yandex.ru",
		'phone': "+7-938-936-1858",
		'langs': "KZ CN EN FR"
	},
	{
		'name': "Jaden Fernandez",
		'age': 47,
		'email': "enim.nisl.elementum@e1.ru",
		'phone': "+7-907-752-6276",
		'langs': "EN FR RU"
	},
	{
		'name': "Teegan Torres",
		'age': 63,
		'email': "proin.non.massa@e1.ru",
		'phone': "+7-952-655-4519",
		'langs': "FR CN KZ"
	},
	{
		'name': "Celeste Frost",
		'age': 27,
		'email': "nam.nulla@ya.ru",
		'phone': "+7-946-887-2581",
		'langs': "FR RU SP"
	},
	{
		'name': "Denton Burnett",
		'age': 29,
		'email': "natoque.penatibus.et@e1.ru",
		'phone': "+7-945-526-3684",
		'langs': "CN RU"
	},
	{
		'name': "Xander Anderson",
		'age': 47,
		'email': "placerat.augue.sed@yandex.ru",
		'phone': "+7-965-368-6217",
		'langs': "SP CN"
	},
	{
		'name': "Rhona Guerrero",
		'age': 23,
		'email': "lacus@yandex.ru",
		'phone': "+7-934-553-4341",
		'langs': "EN"
	},
	{
		'name': "Mariam Harper",
		'age': 26,
		'email': "sed.pharetra@yandex.ru",
		'phone': "+7-983-738-0619",
		'langs': "FR SP CN"
	},
	{
		'name': "Quentin Ramsey",
		'age': 62,
		'email': "a.magna.lorem@mail.ru",
		'phone': "+7-946-014-4579",
		'langs': "RU"
	},
	{
		'name': "Kimberly Matthews",
		'age': 42,
		'email': "ac.mattis.semper@yandex.ru",
		'phone': "+7-976-308-1782",
		'langs': "CN EN FR"
	},
	{
		'name': "George Riddle",
		'age': 44,
		'email': "pede.ultrices.a@e1.ru",
		'phone': "+7-956-223-2574",
		'langs': "SP EN"
	},
	{
		'name': "Aaron Morrison",
		'age': 47,
		'email': "quam.vel@mail.ru",
		'phone': "+7-959-865-2610",
		'langs': "CN FR"
	},
	{
		'name': "Dominic Rosario",
		'age': 23,
		'email': "velit@ya.ru",
		'phone': "+7-913-423-6210",
		'langs': "FR JP"
	},
	{
		'name': "Forrest Briggs",
		'age': 30,
		'email': "eleifend@e1.ru",
		'phone': "+7-969-634-7937",
		'langs': "KZ JP SP FR"
	},
	{
		'name': "Orla Stafford",
		'age': 42,
		'email': "suspendisse.non@e1.ru",
		'phone': "+7-958-106-6811",
		'langs': "JP RU"
	},
	{
		'name': "Carson Livingston",
		'age': 19,
		'email': "mauris.morbi@mail.ru",
		'phone': "+7-924-538-5144",
		'langs': "EN SP"
	},
	{
		'name': "Sonia Becker",
		'age': 28,
		'email': "volutpat.nulla@e1.ru",
		'phone': "+7-938-251-7345",
		'langs': "JP SP EN"
	},
	{
		'name': "Cailin Simpson",
		'age': 21,
		'email': "in@mail.ru",
		'phone': "+7-914-034-1625",
		'langs': "KZ"
	},
	{
		'name': "Germaine Flynn",
		'age': 18,
		'email': "morbi.metus@yandex.ru",
		'phone': "+7-953-632-1768",
		'langs': "JP SP KZ"
	},
	{
		'name': "Alisa Avery",
		'age': 45,
		'email': "laoreet@mail.ru",
		'phone': "+7-933-125-7936",
		'langs': "EN KZ"
	},
	{
		'name': "Connor Stout",
		'age': 46,
		'email': "lacinia.at.iaculis@mail.ru",
		'phone': "+7-992-861-9503",
		'langs': "RU"
	},
	{
		'name': "Rylee Alvarado",
		'age': 45,
		'email': "aliquet.libero@mail.ru",
		'phone': "+7-987-261-5740",
		'langs': "KZ SP EN RU"
	},
	{
		'name': "Patricia Davis",
		'age': 29,
		'email': "habitant.morbi.tristique@ya.ru",
		'phone': "+7-949-752-8386",
		'langs': "KZ"
	},
	{
		'name': "Ferdinand Wolfe",
		'age': 55,
		'email': "nunc.sed@e1.ru",
		'phone': "+7-994-228-1452",
		'langs': "EN"
	},
	{
		'name': "Stewart Donovan",
		'age': 27,
		'email': "vulputate.velit@yandex.ru",
		'phone': "+7-937-807-8742",
		'langs': "FR RU SP JP"
	},
	{
		'name': "Julian Pollard",
		'age': 55,
		'email': "dui.fusce@ya.ru",
		'phone': "+7-958-418-7259",
		'langs': "RU EN"
	},
	{
		'name': "Victoria Mccoy",
		'age': 40,
		'email': "sapien.cursus@ya.ru",
		'phone': "+7-947-587-3842",
		'langs': "SP CN"
	},
	{
		'name': "Jescie Mckay",
		'age': 19,
		'email': "odio.aliquam@yandex.ru",
		'phone': "+7-926-858-3393",
		'langs': "RU"
	},
	{
		'name': "Hoyt Vazquez",
		'age': 58,
		'email': "ultrices@mail.ru",
		'phone': "+7-996-716-8118",
		'langs': "JP SP KZ"
	},
	{
		'name': "Kelsie Clay",
		'age': 45,
		'email': "cursus.et.eros@ya.ru",
		'phone': "+7-953-594-6260",
		'langs': "SP CN EN"
	},
	{
		'name': "Ezekiel Barnett",
		'age': 31,
		'email': "laoreet.posuere.enim@e1.ru",
		'phone': "+7-952-492-1373",
		'langs': "KZ SP"
	},
	{
		'name': "Azalia Ball",
		'age': 47,
		'email': "metus.urna@e1.ru",
		'phone': "+7-955-767-8777",
		'langs': "KZ FR EN JP"
	},
	{
		'name': "Gray Greene",
		'age': 24,
		'email': "sagittis.augue@e1.ru",
		'phone': "+7-907-648-7161",
		'langs': "SP"
	},
	{
		'name': "Iliana Haney",
		'age': 49,
		'email': "ornare.in.faucibus@e1.ru",
		'phone': "+7-929-679-3363",
		'langs': "FR"
	},
	{
		'name': "Matthew Day",
		'age': 19,
		'email': "eros.nec@mail.ru",
		'phone': "+7-954-281-0686",
		'langs': "JP FR"
	},
	{
		'name': "Cassady Williamson",
		'age': 29,
		'email': "vivamus.rhoncus.donec@ya.ru",
		'phone': "+7-912-822-6626",
		'langs': "CN EN RU FR"
	},
	{
		'name': "Sage Finch",
		'age': 42,
		'email': "integer.vulputate.risus@ya.ru",
		'phone': "+7-923-447-2255",
		'langs': "CN KZ SP RU"
	},
	{
		'name': "Karyn Wilkins",
		'age': 50,
		'email': "lorem@e1.ru",
		'phone': "+7-997-186-0958",
		'langs': "CN FR RU SP"
	},
	{
		'name': "Edward Carey",
		'age': 64,
		'email': "et.ipsum@mail.ru",
		'phone': "+7-993-522-7150",
		'langs': "KZ EN RU FR"
	},
	{
		'name': "Illana Holt",
		'age': 39,
		'email': "risus.donec@yandex.ru",
		'phone': "+7-923-008-7877",
		'langs': "KZ SP RU"
	},
	{
		'name': "Hilary Hewitt",
		'age': 20,
		'email': "eu.lacus.quisque@yandex.ru",
		'phone': "+7-914-795-1284",
		'langs': "SP JP CN EN"
	},
	{
		'name': "Rajah Bell",
		'age': 24,
		'email': "viverra.maecenas.iaculis@e1.ru",
		'phone': "+7-913-534-8276",
		'langs': "CN FR SP"
	},
	{
		'name': "Sigourney Mccullough",
		'age': 36,
		'email': "nullam.scelerisque@e1.ru",
		'phone': "+7-922-856-3141",
		'langs': "KZ CN"
	},
	{
		'name': "Yen Howard",
		'age': 40,
		'email': "ullamcorper.duis@e1.ru",
		'phone': "+7-927-594-5543",
		'langs': "RU KZ SP"
	},
	{
		'name': "Fleur Mcknight",
		'age': 25,
		'email': "a.nunc@e1.ru",
		'phone': "+7-975-260-0177",
		'langs': "SP FR JP RU"
	},
	{
		'name': "Giselle Ward",
		'age': 37,
		'email': "duis@yandex.ru",
		'phone': "+7-948-540-3356",
		'langs': "JP KZ"
	},
	{
		'name': "Odette Alvarez",
		'age': 48,
		'email': "lacus.nulla@mail.ru",
		'phone': "+7-914-214-5946",
		'langs': "RU"
	},
	{
		'name': "Portia Everett",
		'age': 28,
		'email': "lorem@e1.ru",
		'phone': "+7-955-652-6134",
		'langs': "SP"
	},
	{
		'name': "Germaine Gibbs",
		'age': 20,
		'email': "proin.nisl@ya.ru",
		'phone': "+7-934-424-5015",
		'langs': "CN KZ JP"
	},
	{
		'name': "Lana Dean",
		'age': 48,
		'email': "egestas.ligula@ya.ru",
		'phone': "+7-923-565-5660",
		'langs': "KZ"
	},
	{
		'name': "Dante Gilliam",
		'age': 30,
		'email': "enim.nec.tempus@ya.ru",
		'phone': "+7-914-426-5131",
		'langs': "EN"
	},
	{
		'name': "Clinton Benjamin",
		'age': 27,
		'email': "turpis.vitae.purus@e1.ru",
		'phone': "+7-983-625-7795",
		'langs': "RU KZ"
	},
	{
		'name': "Rina Schultz",
		'age': 49,
		'email': "orci.lacus@mail.ru",
		'phone': "+7-954-274-8799",
		'langs': "SP FR RU"
	},
	{
		'name': "McKenzie Watson",
		'age': 64,
		'email': "consectetuer.adipiscing.elit@ya.ru",
		'phone': "+7-957-607-9964",
		'langs': "FR RU EN SP"
	},
	{
		'name': "Jolene Schroeder",
		'age': 55,
		'email': "eu@yandex.ru",
		'phone': "+7-955-387-1866",
		'langs': "SP EN"
	},
	{
		'name': "Cathleen Bolton",
		'age': 45,
		'email': "nec.eleifend@mail.ru",
		'phone': "+7-986-477-1436",
		'langs': "FR"
	},
	{
		'name': "Iris Guy",
		'age': 48,
		'email': "senectus.et.netus@ya.ru",
		'phone': "+7-936-856-8124",
		'langs': "FR CN EN"
	},
	{
		'name': "Ginger Green",
		'age': 19,
		'email': "condimentum.donec@e1.ru",
		'phone': "+7-998-021-4557",
		'langs': "FR"
	},
	{
		'name': "Iola Gallegos",
		'age': 41,
		'email': "et.magna@yandex.ru",
		'phone': "+7-938-253-7474",
		'langs': "KZ RU SP"
	},
	{
		'name': "Derek Patel",
		'age': 26,
		'email': "facilisis.non@e1.ru",
		'phone': "+7-943-570-4384",
		'langs': "JP FR"
	},
	{
		'name': "Ginger Chambers",
		'age': 32,
		'email': "egestas.lacinia.sed@mail.ru",
		'phone': "+7-972-863-6373",
		'langs': "KZ CN"
	},
	{
		'name': "Caryn Nelson",
		'age': 30,
		'email': "sit.amet.ornare@mail.ru",
		'phone': "+7-967-254-6746",
		'langs': "FR EN SP JP"
	},
	{
		'name': "Emmanuel Harrell",
		'age': 60,
		'email': "donec.at.arcu@mail.ru",
		'phone': "+7-926-754-7243",
		'langs': "RU SP CN"
	},
	{
		'name': "Nathan Byrd",
		'age': 28,
		'email': "mollis.integer@yandex.ru",
		'phone': "+7-925-333-3588",
		'langs': "FR KZ"
	},
	{
		'name': "Boris Lewis",
		'age': 25,
		'email': "ornare.lectus@mail.ru",
		'phone': "+7-986-355-6268",
		'langs': "EN SP JP"
	},
	{
		'name': "Scott Smith",
		'age': 53,
		'email': "tincidunt.congue@yandex.ru",
		'phone': "+7-992-834-4360",
		'langs': "JP SP"
	},
	{
		'name': "Ethan Peters",
		'age': 62,
		'email': "eu@mail.ru",
		'phone': "+7-942-275-4163",
		'langs': "JP"
	},
	{
		'name': "Ulla Haney",
		'age': 59,
		'email': "tempus.non.lacinia@mail.ru",
		'phone': "+7-963-170-4564",
		'langs': "FR"
	},
	{
		'name': "Lareina Pugh",
		'age': 61,
		'email': "tellus.lorem.eu@ya.ru",
		'phone': "+7-975-224-3715",
		'langs': "SP FR"
	},
	{
		'name': "Tiger Fuentes",
		'age': 63,
		'email': "adipiscing.ligula@e1.ru",
		'phone': "+7-972-346-5764",
		'langs': "KZ EN CN RU"
	},
	{
		'name': "Harrison Buckner",
		'age': 35,
		'email': "consequat.nec@yandex.ru",
		'phone': "+7-989-683-2325",
		'langs': "JP FR CN"
	},
	{
		'name': "Noelle Mason",
		'age': 59,
		'email': "malesuada.augue@e1.ru",
		'phone': "+7-951-629-9153",
		'langs': "FR RU KZ JP"
	},
	{
		'name': "Keaton Quinn",
		'age': 44,
		'email': "arcu.vestibulum@ya.ru",
		'phone': "+7-922-007-7113",
		'langs': "FR CN"
	},
	{
		'name': "Reed Solis",
		'age': 55,
		'email': "eget.tincidunt.dui@ya.ru",
		'phone': "+7-992-331-6474",
		'langs': "JP FR EN"
	},
	{
		'name': "Jaime Ratliff",
		'age': 53,
		'email': "accumsan.laoreet@yandex.ru",
		'phone': "+7-904-314-3252",
		'langs': "EN KZ JP"
	},
	{
		'name': "Shad Burch",
		'age': 29,
		'email': "at.iaculis@ya.ru",
		'phone': "+7-967-154-5717",
		'langs': "SP"
	},
	{
		'name': "Rigel Schwartz",
		'age': 58,
		'email': "quis@e1.ru",
		'phone': "+7-904-552-8375",
		'langs': "FR"
	},
	{
		'name': "Jakeem O'connor",
		'age': 64,
		'email': "dui.suspendisse@ya.ru",
		'phone': "+7-964-618-6097",
		'langs': "KZ JP"
	},
	{
		'name': "Ralph Russell",
		'age': 52,
		'email': "nec.luctus.felis@yandex.ru",
		'phone': "+7-917-715-5581",
		'langs': "SP CN KZ"
	},
	{
		'name': "Ulric Jackson",
		'age': 42,
		'email': "risus.duis@mail.ru",
		'phone': "+7-965-653-5738",
		'langs': "RU SP"
	},
	{
		'name': "Fiona Rhodes",
		'age': 56,
		'email': "consequat@mail.ru",
		'phone': "+7-937-268-9580",
		'langs': "FR SP KZ"
	},
	{
		'name': "Ora Guzman",
		'age': 37,
		'email': "eu@e1.ru",
		'phone': "+7-919-725-2162",
		'langs': "FR CN RU"
	},
	{
		'name': "Hasad Tanner",
		'age': 44,
		'email': "cum.sociis@e1.ru",
		'phone': "+7-942-134-3847",
		'langs': "SP CN"
	},
	{
		'name': "Yoshio Orr",
		'age': 59,
		'email': "nullam.ut.nisi@yandex.ru",
		'phone': "+7-985-273-6886",
		'langs': "SP JP"
	},
	{
		'name': "Conan Alston",
		'age': 61,
		'email': "non.lobortis@yandex.ru",
		'phone': "+7-924-457-4878",
		'langs': "JP FR EN"
	},
	{
		'name': "Hasad Hogan",
		'age': 36,
		'email': "nunc.mauris@e1.ru",
		'phone': "+7-995-660-8414",
		'langs': "CN JP"
	},
	{
		'name': "Jermaine Joseph",
		'age': 25,
		'email': "non.bibendum.sed@yandex.ru",
		'phone': "+7-943-604-7244",
		'langs': "CN SP FR"
	}
]

for person in people:
    langs = set(person['langs'].split())
    if langs >= {'RU', 'CN'}:
        # print(person['name'], person['langs'], sep='\t')
        pass


def knows_ru_cn(person: dict) -> bool:
    langs = set(person['langs'].split())
    return True if langs >= {'RU', 'CN'} else False


people_ru_cn = list(filter(knows_ru_cn, people))
pprint(people_ru_cn)
