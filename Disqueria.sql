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
    insert into interprete values (null,'Laura','Pausini','Italia',null);
    insert into interprete values (null,'Raúl','DiBlasio','Argentina',null);
    insert into interprete values (null,'Richard','Clayderman','Francia',null);
    insert into interprete values (null,'Enya','Brennan','Irlanda',null);
    insert into interprete values (null,'Vangelis','Papathanasiouss','Grecia',null);
    insert into interprete values (null,'Jean Michel','Jarre','Francia',null);
    insert into interprete values (null,'La Mona','Gimenez','Argentina',null);
    insert into interprete values (null,'Chaqueño','Palavecino','Argentina',null);
    insert into interprete values (null,'Hermanos','Pimpinela','Argentina',null);
    insert into interprete values (null,'Ulises','Bueno','Argentina',null);
    insert into interprete values (null,'Leo','Mattioli','Argentina',null);
    insert into interprete values (null,'Carlos','Gardel','Argentina',null);
    insert into interprete values (null,'Aztor','Piazzolla','Argentina',null);
    insert into interprete values (null,'Michael','Jackson','USA',null);
    insert into interprete values (null,'Luis Miguel','Gallego Basteri','Mexico',null);
    insert into interprete values (null,'José Luis','Perales','España',null);
    insert into interprete values (null,'Julio','Iglesias','España',null);
    insert into interprete values (null,'Rosana','Arbelo Gopar','España',null);
    
    use disqueria;
insert into discografica values (null,'BMG'),(null,'Sony Music'),(null,'WEA'),(null,'Universal'),(null,'Independiente');

insert into genero values (null,'Pop'),(null,'Tango'),(null,'Bolero'),(null,'Folklore'),(null,'Instrumental'),(null,'Electrónica');


insert into formato values (null,'Compact Disc'),(null,'Cassette'),(null,'Long Play'),(null,'Digital');

insert into album values (null,1234567,'Lêttre à ma Mère',3,5,10,5,3,'1979-01-01',1000,2,null);
insert into album values (null,1234568,'Las Cosas Que Vives',1,1,12,3,1,'1996-01-01',1000,1,null);
insert into album values (null,1234569,'En Tiempo de Amor',2,5,10,1,1,'1993-01-01',1000,1,null);
insert into album values (null,1234570,'El Piano de América',2,5,10,1,1,'1994-01-01',1000,1,null);


insert into tema values (null,'Lêttre à ma Mère','00:40:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,'Mariage D Amour','00:03:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,"Souvenirs D'Enfance",'00:03:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,"Nostalgie",'00:03:00','Paul De Senneville','Paul De Senneville',1,3);

Use disqueria;
insert into discografica values (null,'Domino Records');
insert into genero values (null,'Rock'),(null, 'Indie');
insert into interprete values (null,'Artic','Monkeys','Inglaterra',null);
insert into album values (null,1234571,'AM',19,8,12,6,1,'2013-09-09',1200,5,null);

insert into tema values (null, 'Do I Wanna Know?', '04:32:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'R U Mine?', '03:20:00', 'Alex Turner, Nick O Malley', 'Alex Turner, Nick O Malley',5,19);
insert into tema values (null, 'One For The Road','03:26:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'Arabella', '03:27:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'I Want It All','03:04:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'No.1 Party Anthem','04:03:00', 'Alex Turner','Alex Turner',5,19);
insert into tema values (null, 'Mad Sounds', '03:35:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'Fireside',' 03:01:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'Whyd You Only Call Me When Youre High?', '02:42:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'Snap Out Of It', '03:12:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'Knee Socks','04:17:00', 'Alex Turner', 'Alex Turner',5,19);
insert into tema values (null, 'I Wanna Be Yours', '03:04:00', 'Alex Turner', 'Alex Turner',5,19);
