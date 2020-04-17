drop database sudoku;
create database sudoku;
use sudoku;
create table start
                   (gno int,
				   col0 int,col1 int,col2 int,col3 int,col4 int,col5 int,col6 int,col7 int,col8 int,
                   col9 int,col10 int,col11 int,col12 int,col13 int,col14 int,col15 int,col16 int,
                   col17 int,col18 int,col19 int,col20 int,col21 int,col22 int,col23 int,col24 int,
                   col25 int,col26 int,col27 int,col28 int,col29 int,col30 int,col31 int,col32 int,
                   col33 int,col34 int,col35 int,col36 int,col37 int,col38 int,col39 int,col40 int,
                   col41 int,col42 int,col43 int,col44 int,col45 int,col46 int,col47 int,col48 int,
                   col49 int,col50 int,col51 int,col52 int,col53 int,col54 int,col55 int,col56 int,
                   col57 int,col58 int,col59 int,col60 int,col61 int,col62 int,col63 int,col64 int,
                   col65 int,col66 int,col67 int,col68 int,col69 int,col70 int,col71 int,col72 int,
                   col73 int,col74 int,col75 int,col76 int,col77 int,col78 int,col79 int,col80 int);
create table solved
                   (gno int,
				   col0 int,col1 int,col2 int,col3 int,col4 int,col5 int,col6 int,col7 int,col8 int,
                   col9 int,col10 int,col11 int,col12 int,col13 int,col14 int,col15 int,col16 int,
                   col17 int,col18 int,col19 int,col20 int,col21 int,col22 int,col23 int,col24 int,
                   col25 int,col26 int,col27 int,col28 int,col29 int,col30 int,col31 int,col32 int,
                   col33 int,col34 int,col35 int,col36 int,col37 int,col38 int,col39 int,col40 int,
                   col41 int,col42 int,col43 int,col44 int,col45 int,col46 int,col47 int,col48 int,
                   col49 int,col50 int,col51 int,col52 int,col53 int,col54 int,col55 int,col56 int,
                   col57 int,col58 int,col59 int,col60 int,col61 int,col62 int,col63 int,col64 int,
                   col65 int,col66 int,col67 int,col68 int,col69 int,col70 int,col71 int,col72 int,
                   col73 int,col74 int,col75 int,col76 int,col77 int,col78 int,col79 int,col80 int);
insert into start values
					(1,
					0, 7, 5, 0, 9, 0, 0, 0, 6,
					0, 2, 3, 0, 8, 0, 0, 4, 0,
					8, 0, 0, 0, 0, 3, 0, 0, 1,
					5, 0, 0, 7, 0, 2, 0, 0, 0,
					0, 4, 0, 8, 0, 6, 0, 2, 0,
					0, 0, 0, 9, 0, 1, 0, 0, 3,
					9, 0, 0, 4, 0, 0, 0, 0, 7,
					0, 6, 0, 0, 7, 0, 5, 8, 0,
					7, 0, 0, 0, 1, 0, 3, 9, 0);
insert into solved values
					(1,
					1, 7, 5, 2, 9, 4, 8, 3, 6,
					6, 2, 3, 1, 8, 7, 9, 4, 5,
					8, 9, 4, 5, 6, 3, 2, 7, 1,
					5, 1, 9, 7, 3, 2, 4, 6, 8,
					3, 4, 7, 8, 5, 6, 1, 2, 9,
					2, 8, 6, 9, 4, 1, 7, 5, 3,
					9, 3, 8, 4, 2, 5, 6, 1, 7,
					4, 6, 1, 3, 7, 9, 5, 8, 2,
					7, 5, 2, 6, 1, 8, 3, 9, 4);
insert into start values
                    (2,
                    5, 1, 7, 6, 0, 0, 0, 3, 4,
                    2, 8, 9, 0, 0, 4, 0, 0, 0,
                    3, 4, 6, 2, 0, 5, 0, 9, 0,
                    6, 0, 2, 0, 0, 0, 0, 1, 0,
                    0, 3, 8, 0, 0, 6, 0, 4, 7,
                    0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 9, 0, 0, 0, 0, 0, 7, 8,
                    7, 0, 3, 4, 0, 0, 5, 6, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0);
insert into solved values
                    (2,
                    5, 1, 7, 6, 9, 8, 2, 3, 4,
                    2, 8, 9, 1, 3, 4, 7, 5, 6,
                    3, 4, 6, 2, 7, 5, 8, 9, 1,
                    6, 7, 2, 8, 4, 9, 3, 1, 5,
                    1, 3, 8, 5, 2, 6, 9, 4, 7,
                    9, 5, 4, 7, 1, 3, 6, 8, 2,
                    4, 9, 5, 3, 6, 2, 1, 7, 8,
                    7, 2, 3, 4, 8, 1, 5, 6, 9,
                    8, 6, 1, 9, 5, 7, 4, 2, 3);
insert into start values
                    (3,
                    8, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 3, 6, 0, 0, 0, 0, 0,
                    0, 7, 0, 0, 9, 0, 2, 0, 0,
                    0, 5, 0, 0, 0, 7, 0, 0, 0,
                    0, 0, 0, 0, 4, 5, 7, 0, 0,
                    0, 0, 0, 1, 0, 0, 0, 3, 0,
                    0, 0, 1, 0, 0, 0, 0, 6, 8,
                    0, 0, 8, 5, 0, 0, 0, 1, 0,
                    0, 9, 0, 0, 0, 0, 4, 0, 0);
insert into solved values
                    (3,
                    8, 1, 2, 7, 5, 3, 6, 4, 9,
                    9, 4, 3, 6, 8, 2, 1, 7, 5,
                    6, 7, 5, 4, 9, 1, 2, 8, 3,
                    1, 5, 4, 2, 3, 7, 8, 9, 6,
                    3, 6, 9, 8, 4, 5, 7, 2, 1,
                    2, 8, 7, 1, 6, 9, 5, 3, 4,
                    5, 2, 1, 9, 7, 4, 3, 6, 8,
                    4, 3, 8, 5, 2, 6, 9, 1, 7,
                    7, 9, 6, 3, 1, 8, 4, 5, 2);
