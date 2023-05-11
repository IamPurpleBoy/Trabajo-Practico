CREATE DATABASE disqueria;

USE disqueria;

CREATE TABLE genero (
id_genero INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50)
);

CREATE TABLE discografica(
    id_discografica INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE formato(
    id_formato INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50)
);

CREATE TABLE interprete(
    id_interprete INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    nacionalidad VARCHAR(50),
    foto VARCHAR(100)
);

create table album(
    id_album int auto_increment primary key,
    cod_album int not null,
    nombre varchar(100) not null,
    id_interprete int not null,
    id_genero int not null,
    cant_temas int not null,
    id_discografica int not null,
    id_formato int not null,
    fec_lanzamiento date,
    precio real not null,
    cantidad int not null,
    caratula varchar(100),
    foreign key(id_genero) references genero(id_genero),
    foreign key(id_discografica) references discografica(id_discografica),
    foreign key(id_formato) references formato(id_formato)
    ); 

create table tema(
        id_tema int auto_increment primary key,
        titulo varchar(100),
        duracion time,
        autor varchar(100) not null,
        compositor varchar(100) not null,
        id_album int,
        id_interprete int,
        foreign key(id_album) references album(id_album),
        foreign key(id_interprete) references interprete(id_interprete)
    );

use disqueria; 
insert into interprete values (null, 'Tini', 'Stoessel', 'argentina',null);
insert into interprete values (null, 'Maria ', 'Becerra', 'argentina',null);
insert into interprete values (null, 'Karol ', 'G', 'colombiana',null); 

use disqueria;
insert into interprete values (null, 'Sin', 'Bandera', 'Mexico-Argentina',null);
insert into interprete values (null, 'Luciano', 'Pereyra', 'Argentina',null);
insert into interprete values (null, 'Estelares', 'Argentina',null);

insert into genero values ( null, 'pop');
insert into genero values ( null, 'regueton');
insert into genero values ( null, 'regueton');
insert into genero values (null,'Balada Romántica'),(null,'Rock Latino'),(null,'Urbano Latino');
 
insert into discografica values (null,'Hollywood Records');
 insert into discografica values (null,'300 Entertainment'); 
 insert into discografica values (null,'UMLE - Latino');
 insert into discografica values (null,'Sony Discos'),(null,'PopArt Discos');
 
insert into formato values (null,'Compact Disc');

insert into album values (null,200, 'Tini Tini Tini',1,1, 14,1,1, '2020-12-03', 1642, 500000,null); 
insert into album values (null,201, 'Animal',2,2, 11,2,1, '2021-08-26', 2900, 00000,null); 
insert into album values (null,202, 'Ocean',3,2, 16,3,1, '2019-05-03', 1472, 00000,null); 

insert into album values (null,203,'De Viaje',16,6,16,6,1,'2003-10-21',1200,4,null);
insert into album values (null,204,'De Hoy En Adelante',17,8,11,4,1,'2022-08-12',1900,3,null);
insert into album values (null,205,'Sistema Nervioso Central',18,7,14,7,1,'2006-09-06',1500,2,null);
 
 
insert into tema values (null, 'Un beso en Madrid', '00:02:24', 'Tini Stoessel y Alejandro Sanz', 'Tini Stoessel, Alejandro Sanz', 1, 1 );
insert into tema values (null, 'Fresa', '00:02:46', 'Tini Stoessel y Lalo Ebratt ', 'Tini Stoessel, Lalo Ebratt', 1, 1 );
insert into tema values (null, 'Si tu supieras', '00:02:32', 'Tini Stoessel', 'Tini Stoessel', 1, 1 );
insert into tema values (null, 'Tuyo', '00:01:54', 'Tini Stoessel', 'Tini Stoessel', 1, 1 );
insert into tema values (null, 'Te olvidaré', '00:03:15', 'Tini Stoessel , Andres Torres y Mauricio Rengifo', 'Tini Stoessel, Andres Torres y Mauricio Rengifo', 1, 1 );
insert into tema values (null, 'Acércate', '00:02:23', 'Tini Stoessel', 'Tini Stoessel', 1, 1);
insert into tema values (null, 'Playa', '00:02:27', 'Tini Stoessel', 'Tini Stoessel', 1, 1 );
insert into tema values (null, 'Ella dice', '00:02:41', 'Tini Stoessel y Khea', 'Tini Stoessel y Khea', 1, 1 );
insert into tema values (null, 'Duele', '00:02:18', 'Tini Stoessel, Andres Torres, Enrique Maroli y Gerardo H.', 'Tini Stoessel, Andres Torres, Enrique Maroli y Gerardo H.', 1, 1 );
insert into tema values (null, 'Recuerdo', '00:03:21', 'Tini Stoessel, Mau y Ricky', 'Tini Stoessel, Mau y Ricky', 1, 1 );
insert into tema values (null, 'Oye', '00:02:53', 'Tini Stoessel y Sebastian Yatra', 'Tini Stoessel, Andrés Torres, MAuricio Rengifo y Sebastian Yatra', 1, 1 );
insert into tema values (null, 'Diciembre', '00:03:09','Tini Stoessel',  'Tini Stoessel,Andres Torres , Francisco Jose Ci´a y  Mauricio Rengifo', 1, 1 );
insert into tema values (null, 'Suéltate el pelo', '00:02:07', 'Tini Stoessel','Tini Stoessel, Andres Torres y  Mauricio Rengifo', 1, 1 );
insert into tema values (null, '22', '00:02:39', 'Tini Stoessel y Greeicy Yeliana Rendon Ceballos','Andres Torres, Greeicy Yeliana Rendon Ceballos, Martina Stoessel y Mauricio Rengifo', 1, 1 );
    
 insert into tema values (null, 'Animal', '00:03:23', 'Maria Becerra y Cazzu', 'Maria Becerra y Cazzu', 2, 2 );
insert into tema values (null, 'A solas', '00:03:36', 'Maria Becerra ', 'Maria Becerra y Big One', 2, 2 );
insert into tema values (null, 'Cerquita de ti', '00:03:14', 'Maria Becerra', 'Maria Becerra', 2, 2 );
insert into tema values (null, 'Acaramelao', '00:03:05', 'Maria Becerra', 'Maria Becerra ', 2, 2 );
insert into tema values (null, 'Cazame', '00:03:19', 'Maria Becerra y Tiago PZK', 'Maria Becerra y Tiago PZK', 2, 2 );
insert into tema values (null, 'Mi debilidad', '00:02:45', 'Maria Becerra', 'Maria Becerra y Big one', 2, 2 );
insert into tema values (null, 'Wow Wow', '00:03:19', 'Maria Becerra y Becky G', 'Maria Becerra y Becky G', 2, 2 );
insert into tema values (null, 'Hace rato', '00:03:13', 'Maria Becerra ', 'Maria Becerra ', 2, 2 );
insert into tema values (null, 'Hipnotiza´', '00:02:29', 'Maria Becerra ', 'Maria Becerra ', 2, 2 );
insert into tema values (null, 'No eres tu soy yo', '00:03:19', 'Maria Becerra y Becky G', 'Maria Becerra y Danny Ocean', 2, 2 );
insert into tema values (null, 'Episodios', '00:02:51', 'Maria Becerra ', 'Maria Becerra ', 2, 2 );


   insert into tema values (null, 'Ocean', '00:02:33', 'Karol G', 'Karol G, Dímelo Flow, Sech, Ovy On The Drums', 3, 3 );
  insert into tema values (null, 'Punto G', '00:03:01', 'Karol G', 'Karol G, Rayito Colombiano, Andy Clay', 3, 3 );
  insert into tema values (null, 'Love with a Quality', '00:03:41', 'Karol G y Damian Marley', 'Ovy On The Drums, Damian Marley', 3, 3 );
  insert into tema values (null, 'Baby', '00:03:58', 'Karol G', 'Karol G, Sky Rompiendo', 3, 3 );
  insert into tema values (null, 'Sin corazón', '00:02:49', 'Karol G', 'Karol G, Anuel AA, DJ Luian, Mambo Kingz, Ovy On The Drums, Héctor Ramos, Miguel Perez, Cristian Colon, Ervin Quiroz', 3, 3 );
  insert into tema values (null, 'Dices que te vas', '00:03:58', 'Karol G y Anuel AA', 'Karol G, Anuel AA, José Manuel Gazmey, José Gazmey Santiago', 3, 3 );
  insert into tema values (null, 'Pineapple', '00:02:58', 'Karol G ', 'Karol G, Sky Rompiendo, Mau y Ricky', 3, 3 );
  insert into tema values (null, 'La vida continuó', '00:02:45', 'Karol G y Simone & Simaria', 'Karol G, Ovy On The Drums, Rafael Silva de Queiroz, The KristoMan', 3, 3 );
  insert into tema values (null, 'Bebesita', '00:03:02', 'Karol G', 'Karol G, Anuel AA, Chris Jeday, Gaby Music, Joan Antonio Gonzalez Marrero, Jorge Cedeño Echevarria, Miguel Antonio Muñoz Rohena', 3, 3 );
  insert into tema values (null, 'Culpables', '00:03:46', 'Karol G y Anuel AA', 'Karol G y Anuel AA', 3, 3 );
  insert into tema values (null, 'Mi cama', '00:02:30', 'Karol G, Nicky Jam y J. Balvin', 'Rayo, Andy Clay, Rene David Cano Rios', 3, 3 );
  insert into tema values (null, 'La ocasión perfecta', '00:03:41', 'Karol G y Yandel', 'Karol G, Ovy On The Drums, Yandel, Jumbo El Que Produce Solo', 3, 3 );
  insert into tema values (null, 'Créeme', '00:03:32', 'Karol G y Maluma', 'Karol G, Maluma', 3, 3 );
  insert into tema values (null, 'Go Karo', '00:02:28', 'Karol G', 'Karol G, Ovy On The Drums, Pato Banton', 3, 3 );
  insert into tema values (null, 'Mi cama (Remix)', '00:03:15', 'Karol G, J Balvin y Nicky Jam)', 'Karol G, Omar Koonze, Rene David Cano Rios, Antonio Rayo, Andy Clay, J Balvin, Nicky Jam', 3, 3 );
  insert into tema values (null, 'Yo aprendí', '00:03:05', 'Karol G y Danay Suárez', '	Karol G, Danay Suárez', 3, 3 );
  

insert into tema values (null,'De Viaje','00:04:14','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Amor Real','00:04:04','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Ven','00:03:43','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'ABC','00:04:31','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Contigo','00:03:59','Leonel Garcia','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Magia','00:04:43','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Bien','00:03:56','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Que Lloro','00:04:02','Leonel Garcia','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Canción Para Los Días Lluviosos','00:03:55','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Mientes Tan Bien','00:03:49','Leonel Garcia','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Puede Ser','00:04:20','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Aquí','00:04:48','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Te Esperare(intro)','00:00:32','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Suficiente','00:03:14','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'Tal Vez','00:06:51','Leonel Garcia y Noel Schajris','Leonel Garcia y Noel Schajris',16,16);
insert into tema values (null,'De Hoy En Adelante','00:00:43','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Me Mentiste','00:02:47','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Te Estás Enamorando De Mí','00:02:43','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Quedate','00:03:16','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Una Mujer Como Tú','00:03:45','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Si No Te Hago Falta','00:06:58','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Como Siempre','00:03:09','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Eres Perfecta','00:02:46','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Para Que Quieres Volver','00:03:08','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Que No Se Le Olvide','00:03:29','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Me Enamoré De Tí','00:04:42','Luciano Pereyra','Luciano Pereyra',17,17);
insert into tema values (null,'Las Vias del Tren','00:03:'48,'Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Eléctricos Duendes','00:03:'41,'Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Un Día Perfecto','00:04:02','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Aire','00:03:36','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Ella Dijo','00:04:44','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'200 Monos','00:04:00','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Jardines Secos','00:04:43','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'El Corazón Sobre Todo','00:03:50','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Un Show','00:04:43','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Luxemburgués','00:04:29','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Buri Buri','00:03:29','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Campanas','00:04:19','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'¿Qué Será?','00:03:47','Manuel Moretti','Manuel Moretti',18,18);
insert into tema values (null,'Ardimos','00:04:37','Manuel Moretti','Manuel Moretti',18,18);