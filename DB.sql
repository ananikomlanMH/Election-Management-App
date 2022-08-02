-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 02 août 2022 à 19:26
-- Version du serveur :  5.7.31
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `election2016`
--
CREATE DATABASE IF NOT EXISTS `election2016` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `election2016`;

-- --------------------------------------------------------

--
-- Structure de la table `bureau`
--

DROP TABLE IF EXISTS `bureau`;
CREATE TABLE IF NOT EXISTS `bureau` (
  `numBureau` int(11) NOT NULL AUTO_INCREMENT,
  `COMMUNE_numCommue` int(11) NOT NULL,
  PRIMARY KEY (`numBureau`,`COMMUNE_numCommue`),
  KEY `fk_BUREAU_COMMUNE1_idx` (`COMMUNE_numCommue`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `candidat`
--

DROP TABLE IF EXISTS `candidat`;
CREATE TABLE IF NOT EXISTS `candidat` (
  `numCandidat` int(11) NOT NULL AUTO_INCREMENT,
  `nomCandidat` varchar(50) NOT NULL,
  `prenomCandidat` varchar(50) NOT NULL,
  `date_naissCandidat` date NOT NULL,
  `lieuNaissCandidat` varchar(50) NOT NULL,
  `genreCandidat` varchar(1) NOT NULL DEFAULT 'M',
  `TYPECANDIDAT_idType` int(11) NOT NULL,
  `PARTI_numParti` int(11) NOT NULL,
  PRIMARY KEY (`numCandidat`,`TYPECANDIDAT_idType`,`PARTI_numParti`),
  KEY `fk_CANDIDAT_TYPECANDIDAT_idx` (`TYPECANDIDAT_idType`),
  KEY `fk_CANDIDAT_PARTI1_idx` (`PARTI_numParti`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `commune`
--

DROP TABLE IF EXISTS `commune`;
CREATE TABLE IF NOT EXISTS `commune` (
  `numCommune` int(11) NOT NULL AUTO_INCREMENT,
  `commune` varchar(50) NOT NULL,
  `DEPARTEMENT_numDepartement` int(11) NOT NULL,
  PRIMARY KEY (`numCommune`,`DEPARTEMENT_numDepartement`),
  UNIQUE KEY `commune_UNIQUE` (`commune`),
  KEY `fk_COMMUNE_DEPARTEMENT1_idx` (`DEPARTEMENT_numDepartement`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `departement`
--

DROP TABLE IF EXISTS `departement`;
CREATE TABLE IF NOT EXISTS `departement` (
  `numDepartement` int(11) NOT NULL AUTO_INCREMENT,
  `departement` varchar(50) NOT NULL,
  `REGION_numRegion` int(11) NOT NULL,
  PRIMARY KEY (`numDepartement`,`REGION_numRegion`),
  UNIQUE KEY `departement_UNIQUE` (`departement`),
  KEY `fk_DEPARTEMENT_REGION1_idx` (`REGION_numRegion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `electeur`
--

DROP TABLE IF EXISTS `electeur`;
CREATE TABLE IF NOT EXISTS `electeur` (
  `numElecteur` int(11) NOT NULL AUTO_INCREMENT,
  `nomElecteur` varchar(50) NOT NULL,
  `prenomElecteur` varchar(50) NOT NULL,
  `dateNaissElecteur` date NOT NULL,
  `genreElecteur` varchar(1) NOT NULL DEFAULT 'M',
  `numPiece` varchar(25) NOT NULL,
  PRIMARY KEY (`numElecteur`),
  UNIQUE KEY `numPiece_UNIQUE` (`numPiece`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `inscrire`
--

DROP TABLE IF EXISTS `inscrire`;
CREATE TABLE IF NOT EXISTS `inscrire` (
  `numBureau` int(11) NOT NULL,
  `numElecteur` int(11) NOT NULL,
  PRIMARY KEY (`numBureau`,`numElecteur`),
  KEY `fk_BUREAU_has_ELECTEUR_ELECTEUR1_idx` (`numElecteur`),
  KEY `fk_BUREAU_has_ELECTEUR_BUREAU1_idx` (`numBureau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `parti`
--

DROP TABLE IF EXISTS `parti`;
CREATE TABLE IF NOT EXISTS `parti` (
  `numParti` int(11) NOT NULL AUTO_INCREMENT,
  `nomParti` varchar(250) NOT NULL,
  PRIMARY KEY (`numParti`),
  UNIQUE KEY `nomParti_UNIQUE` (`nomParti`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_departement_all`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_departement_all`;
CREATE TABLE IF NOT EXISTS `pourcentage_departement_all` (
`voix` decimal(26,2)
,`departement` varchar(50)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_departement_blanc`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_departement_blanc`;
CREATE TABLE IF NOT EXISTS `pourcentage_departement_blanc` (
`voix` decimal(26,2)
,`departement` varchar(50)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_departement_valable`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_departement_valable`;
CREATE TABLE IF NOT EXISTS `pourcentage_departement_valable` (
`voix` decimal(26,2)
,`departement` varchar(50)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_parti_valable`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_parti_valable`;
CREATE TABLE IF NOT EXISTS `pourcentage_parti_valable` (
`voix` decimal(26,2)
,`nomParti` varchar(250)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_region`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_region`;
CREATE TABLE IF NOT EXISTS `pourcentage_region` (
`voix` decimal(26,2)
,`region` varchar(50)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_region_all`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_region_all`;
CREATE TABLE IF NOT EXISTS `pourcentage_region_all` (
`voix` decimal(26,2)
,`region` varchar(50)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_region_blanc`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_region_blanc`;
CREATE TABLE IF NOT EXISTS `pourcentage_region_blanc` (
`voix` decimal(26,2)
,`region` varchar(50)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_region_legislatives`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_region_legislatives`;
CREATE TABLE IF NOT EXISTS `pourcentage_region_legislatives` (
`voix` decimal(26,2)
,`region` varchar(50)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_region_presidentielles`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_region_presidentielles`;
CREATE TABLE IF NOT EXISTS `pourcentage_region_presidentielles` (
`voix` decimal(26,2)
,`region` varchar(50)
);

-- --------------------------------------------------------

--
-- Doublure de structure pour la vue `pourcentage_region_typevote`
-- (Voir ci-dessous la vue réelle)
--
DROP VIEW IF EXISTS `pourcentage_region_typevote`;
CREATE TABLE IF NOT EXISTS `pourcentage_region_typevote` (
`voix` decimal(26,2)
,`typeVote` int(1)
);

-- --------------------------------------------------------

--
-- Structure de la table `region`
--

DROP TABLE IF EXISTS `region`;
CREATE TABLE IF NOT EXISTS `region` (
  `numRegion` int(11) NOT NULL AUTO_INCREMENT,
  `region` varchar(50) NOT NULL,
  PRIMARY KEY (`numRegion`),
  UNIQUE KEY `region_UNIQUE` (`region`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `typecandidat`
--

DROP TABLE IF EXISTS `typecandidat`;
CREATE TABLE IF NOT EXISTS `typecandidat` (
  `idType` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(1) NOT NULL,
  PRIMARY KEY (`idType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `voter`
--

DROP TABLE IF EXISTS `voter`;
CREATE TABLE IF NOT EXISTS `voter` (
  `numCandidat` int(11) NOT NULL AUTO_INCREMENT,
  `numElecteur` int(11) NOT NULL,
  `BUREAU_numBureau` int(11) NOT NULL,
  `Voix` int(1) DEFAULT NULL,
  `Jour` date NOT NULL,
  `Procuration` int(1) NOT NULL,
  `typeVote` int(1) NOT NULL,
  PRIMARY KEY (`numCandidat`,`numElecteur`,`BUREAU_numBureau`),
  KEY `fk_CANDIDAT_has_ELECTEUR_ELECTEUR1_idx` (`numElecteur`),
  KEY `fk_CANDIDAT_has_ELECTEUR_CANDIDAT1_idx` (`numCandidat`),
  KEY `fk_VOTER_BUREAU1_idx` (`BUREAU_numBureau`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_departement_all`
--
DROP TABLE IF EXISTS `pourcentage_departement_all`;

DROP VIEW IF EXISTS `pourcentage_departement_all`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_departement_all`  AS  select round(((count(0) * 100) / (select count(0) from `voter`)),2) AS `voix`,`departement`.`departement` AS `departement` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) group by `departement`.`departement` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_departement_blanc`
--
DROP TABLE IF EXISTS `pourcentage_departement_blanc`;

DROP VIEW IF EXISTS `pourcentage_departement_blanc`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_departement_blanc`  AS  select round(((count(0) * 100) / (select count(0) from `voter` where (`voter`.`Voix` = 0))),2) AS `voix`,`departement`.`departement` AS `departement` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) where (`voter`.`Voix` = 0) group by `departement`.`departement` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_departement_valable`
--
DROP TABLE IF EXISTS `pourcentage_departement_valable`;

DROP VIEW IF EXISTS `pourcentage_departement_valable`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_departement_valable`  AS  select round(((count(0) * 100) / (select count(0) from `voter` where (`voter`.`Voix` = 1))),2) AS `voix`,`departement`.`departement` AS `departement` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) where (`voter`.`Voix` = 1) group by `departement`.`departement` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_parti_valable`
--
DROP TABLE IF EXISTS `pourcentage_parti_valable`;

DROP VIEW IF EXISTS `pourcentage_parti_valable`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_parti_valable`  AS  select round(((count(0) * 100) / (select count(0) from `voter` where (`voter`.`Voix` = 1))),2) AS `voix`,`parti`.`nomParti` AS `nomParti` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) where (`voter`.`Voix` = 1) group by `parti`.`nomParti` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_region`
--
DROP TABLE IF EXISTS `pourcentage_region`;

DROP VIEW IF EXISTS `pourcentage_region`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_region`  AS  select round(((count(0) * 100) / (select count(0) from `voter`)),2) AS `voix`,`region`.`region` AS `region` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) where (`voter`.`Voix` = 1) group by `region`.`numRegion` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_region_all`
--
DROP TABLE IF EXISTS `pourcentage_region_all`;

DROP VIEW IF EXISTS `pourcentage_region_all`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_region_all`  AS  select round(((count(0) * 100) / (select count(0) from `voter`)),2) AS `voix`,`region`.`region` AS `region` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) group by `region`.`numRegion` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_region_blanc`
--
DROP TABLE IF EXISTS `pourcentage_region_blanc`;

DROP VIEW IF EXISTS `pourcentage_region_blanc`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_region_blanc`  AS  select round(((count(0) * 100) / (select count(0) from `voter`)),2) AS `voix`,`region`.`region` AS `region` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) where (`voter`.`Voix` = 0) group by `region`.`numRegion` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_region_legislatives`
--
DROP TABLE IF EXISTS `pourcentage_region_legislatives`;

DROP VIEW IF EXISTS `pourcentage_region_legislatives`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_region_legislatives`  AS  select round(((count(0) * 100) / (select count(0) from `voter` where ((`voter`.`Voix` = 1) and (`voter`.`typeVote` = 1)))),2) AS `voix`,`region`.`region` AS `region` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) where ((`voter`.`Voix` = 1) and (`voter`.`typeVote` = 1)) group by `region`.`numRegion` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_region_presidentielles`
--
DROP TABLE IF EXISTS `pourcentage_region_presidentielles`;

DROP VIEW IF EXISTS `pourcentage_region_presidentielles`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_region_presidentielles`  AS  select round(((count(0) * 100) / (select count(0) from `voter` where ((`voter`.`Voix` = 1) and (`voter`.`typeVote` = 0)))),2) AS `voix`,`region`.`region` AS `region` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) where ((`voter`.`Voix` = 1) and (`voter`.`typeVote` = 0)) group by `region`.`numRegion` ;

-- --------------------------------------------------------

--
-- Structure de la vue `pourcentage_region_typevote`
--
DROP TABLE IF EXISTS `pourcentage_region_typevote`;

DROP VIEW IF EXISTS `pourcentage_region_typevote`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `pourcentage_region_typevote`  AS  select round(((count(0) * 100) / (select count(0) from `voter` where (`voter`.`Voix` = 1))),2) AS `voix`,`voter`.`typeVote` AS `typeVote` from ((((((((`candidat` join `voter` on((`voter`.`numCandidat` = `candidat`.`numCandidat`))) join `electeur` on((`electeur`.`numElecteur` = `voter`.`numElecteur`))) join `bureau` on((`bureau`.`numBureau` = `voter`.`BUREAU_numBureau`))) join `commune` on((`commune`.`numCommune` = `bureau`.`COMMUNE_numCommue`))) join `departement` on((`departement`.`numDepartement` = `commune`.`DEPARTEMENT_numDepartement`))) join `region` on((`region`.`numRegion` = `departement`.`REGION_numRegion`))) join `parti` on((`parti`.`numParti` = `candidat`.`PARTI_numParti`))) join `typecandidat` on((`typecandidat`.`idType` = `candidat`.`TYPECANDIDAT_idType`))) where (`voter`.`Voix` = 1) group by `voter`.`typeVote` ;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `bureau`
--
ALTER TABLE `bureau`
  ADD CONSTRAINT `fk_BUREAU_COMMUNE1` FOREIGN KEY (`COMMUNE_numCommue`) REFERENCES `commune` (`numCommune`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `candidat`
--
ALTER TABLE `candidat`
  ADD CONSTRAINT `fk_CANDIDAT_PARTI` FOREIGN KEY (`PARTI_numParti`) REFERENCES `parti` (`numParti`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_CANDIDAT_TYPECANDIDAT` FOREIGN KEY (`TYPECANDIDAT_idType`) REFERENCES `typecandidat` (`idType`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `commune`
--
ALTER TABLE `commune`
  ADD CONSTRAINT `fk_COMMUNE_DEPARTEMENT1` FOREIGN KEY (`DEPARTEMENT_numDepartement`) REFERENCES `departement` (`numDepartement`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `departement`
--
ALTER TABLE `departement`
  ADD CONSTRAINT `fk_DEPARTEMENT_REGION1` FOREIGN KEY (`REGION_numRegion`) REFERENCES `region` (`numRegion`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `inscrire`
--
ALTER TABLE `inscrire`
  ADD CONSTRAINT `fk_BUREAU_has_ELECTEUR_BUREAU1` FOREIGN KEY (`numBureau`) REFERENCES `bureau` (`numBureau`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_BUREAU_has_ELECTEUR_ELECTEUR1` FOREIGN KEY (`numElecteur`) REFERENCES `electeur` (`numElecteur`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `voter`
--
ALTER TABLE `voter`
  ADD CONSTRAINT `fk_CANDIDAT_has_ELECTEUR_CANDIDAT1` FOREIGN KEY (`numCandidat`) REFERENCES `candidat` (`numCandidat`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_CANDIDAT_has_ELECTEUR_ELECTEUR1` FOREIGN KEY (`numElecteur`) REFERENCES `electeur` (`numElecteur`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_VOTER_BUREAU1` FOREIGN KEY (`BUREAU_numBureau`) REFERENCES `bureau` (`numBureau`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
