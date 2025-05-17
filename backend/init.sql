--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

-- Started on 2025-05-17 19:00:51

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 45901)
-- Name: words; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.words (
    id integer NOT NULL,
    word text NOT NULL,
    clue text NOT NULL
);


ALTER TABLE public.words OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 45900)
-- Name: words_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.words_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.words_id_seq OWNER TO postgres;

--
-- TOC entry 4852 (class 0 OID 0)
-- Dependencies: 217
-- Name: words_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.words_id_seq OWNED BY public.words.id;


--
-- TOC entry 4695 (class 2604 OID 45904)
-- Name: words id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.words ALTER COLUMN id SET DEFAULT nextval('public.words_id_seq'::regclass);


--
-- TOC entry 4846 (class 0 OID 45901)
-- Dependencies: 218
-- Data for Name: words; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.words (id, word, clue) FROM stdin;
6	КУЛИБИН	Русский механик-изобретатель автоматических часов и оптических приборов.   
7	ПОЛЗУНОВ	Первый в России создатель двухцилиндрового парового двигателя.
8	ЭЙЛЕР	Швейцарский математик, приглашённый в Петербургскую академию наук
9	ЛОМОНОСОВ	Российский энциклопедист XVIII века, основатель Московского университета.   
10	КРАШЕНИННИКОВ	Учёный, описавший природу Камчатки в экспедиции Беринга.
11	СЕНАТ	Высший орган власти, созданный Петром I в 1711 году.
12	АССАМБЛЕИ	Светские собрания, введённые Петром I.
13	ТАБАК	Продукт, распространение которого поощрял Пётр I.
14	РЕДУТ	 Полевое укрепление, использовавшееся в сражениях.
15	АРТИЛЛЕРИЯ	Род войск, ставший ключевым после победы под Полтавой.
16	ФЕАТРОН	Первый публичный театр в России при Петре I.
17	БАЛТИКА	Море, ставшее центром морских сил после Северной войны.
18	АРКТИКА	Регион, исследованный экспедициями по указу Петра I.
19	РИХМАН	Физик, погибший во время экспериментов с атмосферным электричеством.
20	АТМОСФЕРА	Воздушная оболочка планет, открытая Ломоносовым на примере Венеры
21	МАНУФАКТУРА	Предприятие по производству товаров вручную или с помощью машин.   
22	ПРОСВЕЩЕНИЕ	Эпоха, давшая название идеям развития науки и образования.   
23	РЕФОРМА	Изменения в государственном устройстве. 
24	НАУКА	 Система знаний, поддерживаемая Академией и государством в XVIII в.   
25	ШРИФТ	Новый гражданский стиль письма, введённый Петром I.   
26	БЕРГПРИВИЛЕГИЯ	Право на добычу полезных ископаемых, введённое в 1719 г.   
27	ФЛОТ	Военно-морской контингент, реформированный Петром I.   
28	КАМЧАТКА	Полуостров, изученный экспедицией Беринга.
29	СИБИРЬ	Регион, исследованный во Второй Камчатской экспедиции.   
30	ШПИТАЛЬ	Военный госпиталь с аптекой, учреждённый Петром I.   
31	БАНЯ	Русская традиция омовения, на которую был введён налог Петром I.   
32	ВЕДОМОСТИ	Первая ежедневная русская газета, издававшаяся с 1702 г.   
34	ЭКСПЕДИЦИЯ	 Научное путешествие, как Вторая Камчатская экспедиция Беринга.   
35	ГЕОЛОГИЯ	Наука о строении Земли; Ломоносов участвовал в минералогических исследованиях.   
36	ФИЛОЛОГИЯ	Гуманитарная дисциплина; Ломоносов внёс вклад в развитие русского языка.   
37	ФИЗИКА	Естественная наука; Ломоносов разработал молекулярно-кинетическую теорию тепла.   
38	ХИМИЯ	Наука, одним из основателей которой в России считается Ломоносов.   
39	МЕТЕОРОЛОГИЯ	Наука о погоде; Ломоносов сконструировал первые метеоприборы.
40	АСТРОНОМИЯ	Наука о небесных телах, развитая Брюсом и Рихманом.   
41	МИНЕРАЛОГИЯ	Наука о минералах; Ломоносов составил первый каталог коллекций.   
42	ГИМНАЗИЯ	Предуниверситетское учебное заведение при Петербургской академии.   
43	КУНСТКАМЕРА	Первый русский музей редкостей, открытый в 1719 г.   
44	УНИВЕРСИТЕТ	Учебное заведение, основанное в 1755 г. по проекту Ломоносова.
45	АКАДЕМИЯ	Научный центр, основанный Петром I в 1724 году.   
46	ДАШКОВА	Покровительница науки и образования при Екатерине II.   
\.


--
-- TOC entry 4853 (class 0 OID 0)
-- Dependencies: 217
-- Name: words_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.words_id_seq', 46, true);


--
-- TOC entry 4697 (class 2606 OID 45908)
-- Name: words words_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.words
    ADD CONSTRAINT words_pkey PRIMARY KEY (id);


--
-- TOC entry 4699 (class 2606 OID 45910)
-- Name: words words_word_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.words
    ADD CONSTRAINT words_word_key UNIQUE (word);


-- Completed on 2025-05-17 19:00:52

--
-- PostgreSQL database dump complete
--

