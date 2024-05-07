-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 07 May 2024, 22:01:04
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `python_oyun`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `admins`
--

CREATE TABLE `admins` (
  `id` int(11) NOT NULL,
  `kullanici_adi` text NOT NULL,
  `sifre` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `admins`
--

INSERT INTO `admins` (`id`, `kullanici_adi`, `sifre`) VALUES
(1, 'emre', 'emre');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullanicilar`
--

CREATE TABLE `kullanicilar` (
  `id` int(11) NOT NULL,
  `kullanici_adi` text NOT NULL,
  `numara` text NOT NULL,
  `sifre` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `kullanicilar`
--

INSERT INTO `kullanicilar` (`id`, `kullanici_adi`, `numara`, `sifre`) VALUES
(1, '1', '1', '1'),
(2, 'q', 'q', 'q'),
(3, 'ahmet', '55123121', '123'),
(4, '12', '12', '12');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `oyunlar`
--

CREATE TABLE `oyunlar` (
  `oyun_id` int(11) NOT NULL,
  `Oyun_adi` text NOT NULL,
  `turu` text NOT NULL,
  `platform` text NOT NULL,
  `alan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `oyunlar`
--

INSERT INTO `oyunlar` (`oyun_id`, `Oyun_adi`, `turu`, `platform`, `alan`) VALUES
(1, 'Minecraft', 'Macera', 'PC/KONSOL', ''),
(3, 'GTA', 'Aksiyon', 'PC/KONSOL', '2'),
(5, 'Valorant', 'Aksiyon', 'PC', '1');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yorumlar`
--

CREATE TABLE `yorumlar` (
  `yorum` text NOT NULL,
  `puan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `yorumlar`
--

INSERT INTO `yorumlar` (`yorum`, `puan`) VALUES
('Hayatımda oynadığım en iyi oyun!', '5'),
('ÇOK İYİ!', '5'),
('Peh..', '3'),
('Çok iyi!!', '5'),
('İdare eder.', '3'),
('Yaniiii.', '3'),
('Koşma efekti çok kötü.', '2'),
('Çöp', '1'),
('OHA!', '5'),
('süper', '5'),
('süper', '10'),
('yok beğğ', '5');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yorumlar_gta`
--

CREATE TABLE `yorumlar_gta` (
  `Yorum` text NOT NULL,
  `Puan` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `yorumlar_gta`
--

INSERT INTO `yorumlar_gta` (`Yorum`, `Puan`) VALUES
('Yani fazla iyi değil.', '3'),
('Açık dünya severler için güzel.', '4'),
('SÜPERRRRR!', '5'),
('SÜPERRRRR!', '5'),
('OHA YANİ', '5'),
('ee bune yani?', '1'),
('beğenmedim.', '1'),
('süper', '4'),
('bok gibi', '1'),
('çok güzel beğendim', '1');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `yorumlar_valo`
--

CREATE TABLE `yorumlar_valo` (
  `Yorum` text NOT NULL,
  `Puan` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `yorumlar_valo`
--

INSERT INTO `yorumlar_valo` (`Yorum`, `Puan`) VALUES
('SÜPER!!', 5),
('TAM BİR AKSİYON OYUNU!', 5),
('KÖTÜ', 1);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `admins`
--
ALTER TABLE `admins`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kullanicilar`
--
ALTER TABLE `kullanicilar`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `oyunlar`
--
ALTER TABLE `oyunlar`
  ADD PRIMARY KEY (`oyun_id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `admins`
--
ALTER TABLE `admins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `kullanicilar`
--
ALTER TABLE `kullanicilar`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Tablo için AUTO_INCREMENT değeri `oyunlar`
--
ALTER TABLE `oyunlar`
  MODIFY `oyun_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
