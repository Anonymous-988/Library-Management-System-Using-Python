-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 06, 2023 at 08:41 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `itemid` int(11) NOT NULL,
  `itemtype` varchar(50) NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(50) DEFAULT NULL,
  `pyear` year(4) NOT NULL,
  `quantity` int(11) NOT NULL,
  `genre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`itemid`, `itemtype`, `title`, `author`, `pyear`, `quantity`, `genre`) VALUES
(72, 'book', 'Red Roses', 'Prem Dev', 1991, 2, 'Romance'),
(73, 'book', 'Indiana Holmes', 'Sachin Ray', 1995, 2, 'Thriller'),
(74, 'book', 'Faulty Stars', 'Pyaari Kumari', 2011, 1, 'Romance'),
(75, 'book', 'Hero 007', 'Mahesh Bhat', 2010, 6, 'Action'),
(76, 'book', 'Khiladi', 'Bhanu Pandey', 2001, 5, 'Action'),
(77, 'journal', 'Nanophotonics', NULL, 1990, 3, 'Physics'),
(78, 'journal', 'Physics RevC', NULL, 1975, 1, 'Physics'),
(79, 'journal', 'EcoMoney', NULL, 2001, 1, 'Economics'),
(80, 'journal', 'Econometricia', NULL, 2009, 2, 'Economics');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `fname`, `lname`, `email`, `password`) VALUES
(21, 'Sumant', 'Pujari', 'Sumant11', '21122112'),
(25, 'NA', 'NA', 'admin', '9881257715');

-- --------------------------------------------------------

--
-- Table structure for table `user_action`
--

CREATE TABLE `user_action` (
  `aid` int(11) NOT NULL,
  `uid` int(11) DEFAULT NULL,
  `itemid` int(11) DEFAULT NULL,
  `action` varchar(50) NOT NULL,
  `rating` int(11) DEFAULT NULL,
  `review` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_action`
--

INSERT INTO `user_action` (`aid`, `uid`, `itemid`, `action`, `rating`, `review`) VALUES
(100, 21, 73, 'Borrow', NULL, NULL),
(101, 21, 76, 'Return', 4, 'Noice');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`itemid`),
  ADD UNIQUE KEY `title` (`title`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `user_action`
--
ALTER TABLE `user_action`
  ADD PRIMARY KEY (`aid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `itemid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `user_action`
--
ALTER TABLE `user_action`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
