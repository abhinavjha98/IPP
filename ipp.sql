-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2019 at 11:18 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.2.24

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ipp`
--

-- --------------------------------------------------------

--
-- Table structure for table `company_master_table`
--

CREATE TABLE `company_master_table` (
  `Sr_No` int(25) NOT NULL,
  `Name_of_Company` varchar(25) NOT NULL,
  `Company_ID` int(25) NOT NULL,
  `Month` varchar(25) NOT NULL,
  `Unit` int(25) NOT NULL,
  `Address` varchar(25) NOT NULL,
  `State` varchar(20) NOT NULL,
  `PinCode` int(20) NOT NULL,
  `Customer_Contact_Person` int(25) NOT NULL,
  `Customer_Contact_Number` int(25) NOT NULL,
  `Supervisor` varchar(25) NOT NULL,
  `Reporting_1` varchar(25) NOT NULL,
  `Reporting_2` varchar(25) NOT NULL,
  `Reporting_3` varchar(25) NOT NULL,
  `Reporting_4` varchar(25) NOT NULL,
  `Reporting_5` varchar(25) NOT NULL,
  `Closed_By` varchar(25) NOT NULL,
  `Services_A` varchar(25) NOT NULL,
  `Services_Model` varchar(25) NOT NULL,
  `Reputation_of_client` double NOT NULL,
  `Service_Charges` double NOT NULL,
  `Actual_Stipend` double NOT NULL,
  `Working_Condition` double NOT NULL,
  `Facilities` double NOT NULL,
  `others` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company_master_table`
--

INSERT INTO `company_master_table` (`Sr_No`, `Name_of_Company`, `Company_ID`, `Month`, `Unit`, `Address`, `State`, `PinCode`, `Customer_Contact_Person`, `Customer_Contact_Number`, `Supervisor`, `Reporting_1`, `Reporting_2`, `Reporting_3`, `Reporting_4`, `Reporting_5`, `Closed_By`, `Services_A`, `Services_Model`, `Reputation_of_client`, `Service_Charges`, `Actual_Stipend`, `Working_Condition`, `Facilities`, `others`) VALUES
(1, 'Pape_Audio', 1001, 'January', 123, 'pune', 'maharashtra', 411035, 0, 9766, 'Super', 'y', 'n', 'n', 'n', 'n', 'Y', 'NEEM', 'OP', 0, 1.5, 1, 1.5, 1, 1),
(2, 'Amigo_Hospitality', 1002, 'February', 254, 'pune', 'maharashtra', 411035, 0, 9766, 'Super', 'N', 'Y', 'y', 'y', 'n', 'y', 'NAPS', 'SRP', 0, 1, 1.5, 1.5, 1, 1),
(3, 'RVC_Logistics', 1003, 'February', 254, 'pune', 'maharashtra', 411035, 0, 9766, 'Super', 'N', 'Y', 'y', 'y', 'n', 'y', 'NAPS', 'SRP', 0, 1, 1, 1, 1.5, 1);

-- --------------------------------------------------------

--
-- Table structure for table `company_table`
--

CREATE TABLE `company_table` (
  `comp_name` varchar(30) NOT NULL,
  `comp_uid` varchar(20) NOT NULL,
  `comp_address` varchar(30) NOT NULL,
  `comp_location` varchar(25) NOT NULL,
  `comp_GSTN` varchar(25) NOT NULL,
  `comp_description` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `company_table`
--

INSERT INTO `company_table` (`comp_name`, `comp_uid`, `comp_address`, `comp_location`, `comp_GSTN`, `comp_description`) VALUES
('asd', 'e01', 'G78 Mecords India Ltd. MIDC,, ', 'pune', 'e12344', '231123'),
('asd', 'e01', 'G78 Mecords India Ltd. MIDC,, ', 'pune', 'e12344', '231123'),
('asd', '213', 'BNO.3 FNO.01,BHAKTI PARK,SUSHI', 'pune', 'e12344', '231123');

-- --------------------------------------------------------

--
-- Table structure for table `dod_table`
--

CREATE TABLE `dod_table` (
  `reputation_client` varchar(30) NOT NULL,
  `training_fee` int(20) NOT NULL,
  `stipend` int(20) NOT NULL,
  `working_condition` int(20) NOT NULL,
  `transport_canteen_facility` int(20) NOT NULL,
  `others` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dod_table`
--

INSERT INTO `dod_table` (`reputation_client`, `training_fee`, `stipend`, `working_condition`, `transport_canteen_facility`, `others`) VALUES
('4', 4, 1, 33, 33, 34),
('12', 33, 13, 34, 4, 5),
('4', 1, 45, 145, 5, 15),
('4', 4, 1, 33, 33, 34),
('12', 33, 13, 34, 4, 5),
('2', 1, 45, 145, 5, 15),
('4', 4, 1, 33, 33, 34),
('12', 33, 13, 34, 4, 5),
('2', 1, 45, 145, 5, 15),
('T02', 1, 3, 45, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `employee_master`
--

CREATE TABLE `employee_master` (
  `Sr_No` int(25) NOT NULL,
  `Prepared_By` varchar(25) NOT NULL,
  `Code` varchar(25) NOT NULL,
  `Emp_No` varchar(25) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Gender` varchar(25) NOT NULL,
  `Father_Name` varchar(25) NOT NULL,
  `DOB` varchar(25) NOT NULL,
  `DOJ` varchar(25) NOT NULL,
  `Paid_By` varchar(25) NOT NULL,
  `Cost_Centre` varchar(25) NOT NULL,
  `Employee_Name_On_Passbook` varchar(25) NOT NULL,
  `Bank_Name` varchar(25) NOT NULL,
  `Branch_Name` varchar(25) NOT NULL,
  `IFSC_Code` varchar(25) NOT NULL,
  `Beneficiary_Account_Number` varchar(25) NOT NULL,
  `Beneficiary_City` varchar(25) NOT NULL,
  `State` varchar(25) NOT NULL,
  `email_address` varchar(25) NOT NULL,
  `pay_days` int(25) NOT NULL,
  `total_days` int(25) NOT NULL,
  `location` varchar(25) NOT NULL,
  `Bank_State` varchar(25) NOT NULL,
  `CPI_eligibility` varchar(25) NOT NULL,
  `Designation` varchar(25) NOT NULL,
  `ODOJ` varchar(25) NOT NULL,
  `Level` varchar(25) NOT NULL,
  `Direct_Indirect` varchar(25) NOT NULL,
  `Reporting_1` varchar(25) NOT NULL,
  `Reporting_2` varchar(25) NOT NULL,
  `Reporting_3` varchar(25) NOT NULL,
  `Reporting_4` varchar(25) NOT NULL,
  `Reporting_5` varchar(25) NOT NULL,
  `Personal_Official_No` int(25) NOT NULL,
  `Company` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee_master`
--

INSERT INTO `employee_master` (`Sr_No`, `Prepared_By`, `Code`, `Emp_No`, `Name`, `Gender`, `Father_Name`, `DOB`, `DOJ`, `Paid_By`, `Cost_Centre`, `Employee_Name_On_Passbook`, `Bank_Name`, `Branch_Name`, `IFSC_Code`, `Beneficiary_Account_Number`, `Beneficiary_City`, `State`, `email_address`, `pay_days`, `total_days`, `location`, `Bank_State`, `CPI_eligibility`, `Designation`, `ODOJ`, `Level`, `Direct_Indirect`, `Reporting_1`, `Reporting_2`, `Reporting_3`, `Reporting_4`, `Reporting_5`, `Personal_Official_No`, `Company`) VALUES
(1, 'AP', 'Y', 'MEL014', 'Mahesh Jamadar', 'Male', 'NA', '06-Jun-82', '01-Mar-16', 'MPTA', 'OJT', 'Maheshkumar Madhukar Jama', 'State Bank of India', 'Jule Solapur', 'SBIN0012485', '31025955248', 'PUNE', 'Maharashtra', 'maheshjamadar23@gmail.com', 31, 31, 'Kirloskar Ferrous Industr', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '01-Mar-11', '1', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 4545, 'Pape Audio'),
(2, 'AP', 'Y', 'MEL016', 'Gopinath Shesherao Jadhav', 'Male', 'NA', '25-Sep-88', '01-Aug-18', 'MPTA', 'OJT', 'Gopinath Shesherao Jadhav', 'State Bank of India', 'Erandawane', 'SBIN0004618', '20084105393', 'PUNE', 'Maharashtra', 'gopinath.jdh88@gmail.com', 31, 31, 'Harman International', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '14-Apr-11', '1', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 52152, 'Pape Audio'),
(3, 'AP', 'Y', 'MEL014', 'Mahesh Jamadar', 'Male', 'NA', '06-Jun-82', '01-Mar-16', 'MPTA', 'OJT', 'Maheshkumar Madhukar Jama', 'State Bank of India', 'Jule Solapur', 'SBIN0012485', '31025955248', 'PUNE', 'Maharashtra', 'maheshjamadar23@gmail.com', 31, 31, 'Kirloskar Ferrous Industr', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '01-Mar-11', '2', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 4545, 'Pape Audio'),
(4, 'AP', 'Y', 'MEL016', 'Gopinath Shesherao Jadhav', 'Male', 'NA', '25-Sep-88', '01-Aug-18', 'MPTA', 'OJT', 'Gopinath Shesherao Jadhav', 'State Bank of India', 'Erandawane', 'SBIN0004618', '20084105393', 'PUNE', 'Maharashtra', 'gopinath.jdh88@gmail.com', 31, 31, 'Harman International', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '14-Apr-11', '2', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 52152, 'Pape Audio'),
(5, 'AP', 'Y', 'MEL014', 'Mahesh Jamadar', 'Male', 'NA', '06-Jun-82', '01-Mar-16', 'MPTA', 'OJT', 'Maheshkumar Madhukar Jama', 'State Bank of India', 'Jule Solapur', 'SBIN0012485', '31025955248', 'PUNE', 'Maharashtra', 'maheshjamadar23@gmail.com', 31, 31, 'Kirloskar Ferrous Industr', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '01-Mar-11', '1', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 4545, 'Pape Audio'),
(6, 'AP', 'Y', 'MEL016', 'Gopinath Shesherao Jadhav', 'Male', 'NA', '25-Sep-88', '01-Aug-18', 'MPTA', 'OJT', 'Gopinath Shesherao Jadhav', 'State Bank of India', 'Erandawane', 'SBIN0004618', '20084105393', 'PUNE', 'Maharashtra', 'gopinath.jdh88@gmail.com', 31, 31, 'Harman International', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '14-Apr-11', '1', 'Indirect', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 52152, 'Pape Audio'),
(7, 'AP', 'Y', 'MEL014', 'Mahesh Jamadar', 'Male', 'NA', '06-Jun-82', '01-Mar-16', 'MPTA', 'OJT', 'Maheshkumar Madhukar Jama', 'State Bank of India', 'Jule Solapur', 'SBIN0012485', '31025955248', 'PUNE', 'Maharashtra', 'maheshjamadar23@gmail.com', 31, 31, 'Kirloskar Ferrous Industr', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '01-Mar-11', '1', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 4545, 'Amigo Hospitality'),
(8, 'AP', 'Y', 'MEL016', 'Gopinath Shesherao Jadhav', 'Male', 'NA', '25-Sep-88', '01-Aug-18', 'MPTA', 'OJT', 'Gopinath Shesherao Jadhav', 'State Bank of India', 'Erandawane', 'SBIN0004618', '20084105393', 'PUNE', 'Maharashtra', 'gopinath.jdh88@gmail.com', 31, 31, 'Harman International', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '14-Apr-11', '1', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 52152, 'Amigo Hospitality'),
(9, 'AP', 'Y', 'MEL014', 'Mahesh Jamadar', 'Male', 'NA', '06-Jun-82', '01-Mar-16', 'MPTA', 'OJT', 'Maheshkumar Madhukar Jama', 'State Bank of India', 'Jule Solapur', 'SBIN0012485', '31025955248', 'PUNE', 'Maharashtra', 'maheshjamadar23@gmail.com', 31, 31, 'Kirloskar Ferrous Industr', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '01-Mar-11', '2', 'Indirect', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 4545, 'Amigo Hospitality'),
(10, 'AP', 'Y', 'MEL016', 'Gopinath Shesherao Jadhav', 'Male', 'NA', '25-Sep-88', '01-Aug-18', 'MPTA', 'OJT', 'Gopinath Shesherao Jadhav', 'State Bank of India', 'Erandawane', 'SBIN0004618', '20084105393', 'PUNE', 'Maharashtra', 'gopinath.jdh88@gmail.com', 31, 31, 'Harman International', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '14-Apr-11', '1', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 52152, 'Amigo Hospitality'),
(11, 'AP', 'Y', 'MEL014', 'Mahesh Jamadar', 'Male', 'NA', '06-Jun-82', '01-Mar-16', 'MPTA', 'OJT', 'Maheshkumar Madhukar Jama', 'State Bank of India', 'Jule Solapur', 'SBIN0012485', '31025955248', 'PUNE', 'Maharashtra', 'maheshjamadar23@gmail.com', 31, 31, 'Kirloskar Ferrous Industr', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '01-Mar-11', '2', 'Indirect', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 4545, 'RVC Logistics'),
(12, 'AP', 'Y', 'MEL016', 'Gopinath Shesherao Jadhav', 'Male', 'NA', '25-Sep-88', '01-Aug-18', 'MPTA', 'OJT', 'Gopinath Shesherao Jadhav', 'State Bank of India', 'Erandawane', 'SBIN0004618', '20084105393', 'PUNE', 'Maharashtra', 'gopinath.jdh88@gmail.com', 31, 31, 'Harman International', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '14-Apr-11', '1', 'Direct', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 52152, 'RVC Logistics'),
(13, 'AP', 'Y', 'MEL016', 'Gopinath Shesherao Jadhav', 'Male', 'NA', '25-Sep-88', '01-Aug-18', 'MPTA', 'OJT', 'Gopinath Shesherao Jadhav', 'State Bank of India', 'Erandawane', 'SBIN0004618', '20084105393', 'PUNE', 'Maharashtra', 'gopinath.jdh88@gmail.com', 31, 31, 'Harman International', 'Maharashtra', 'Direct1', 'Sr. Supervisor', '14-Apr-11', '2', 'Indirect', 'Somwanshi Ranjeet', 'Sheshadri Bhirdikar', 'Sadanand Deshpande', '', '', 52152, 'RVC Logistics');

-- --------------------------------------------------------

--
-- Table structure for table `ipp_company`
--

CREATE TABLE `ipp_company` (
  `Company_ID` int(25) NOT NULL,
  `Name_of_Company` varchar(25) NOT NULL,
  `Months` varchar(25) NOT NULL,
  `Services` varchar(25) NOT NULL,
  `Unit` int(25) NOT NULL,
  `Invoice_Value` int(25) NOT NULL,
  `IPP` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ipp_company`
--

INSERT INTO `ipp_company` (`Company_ID`, `Name_of_Company`, `Months`, `Services`, `Unit`, `Invoice_Value`, `IPP`) VALUES
(1001, 'Pape_Audio', 'January', 'NAPS', 4300, 215000, 2257.5),
(1002, 'Amigo_Hospitality', 'January', 'NAPS', 3300, 165000, 1732.5),
(1003, 'RVC_Logistics', 'January', 'NAPS', 7600, 380000, 2660);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `FirstName` varchar(25) NOT NULL,
  `LastName` varchar(25) NOT NULL,
  `emailid` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`FirstName`, `LastName`, `emailid`, `password`) VALUES
('Abhinav', 'Jha', 'abhinavjha98ald@gmail.com', 'admin'),
('admin', 'admin', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `services_invoice`
--

CREATE TABLE `services_invoice` (
  `Sr_No` int(25) NOT NULL,
  `Name_of_Company` varchar(25) NOT NULL,
  `Company_ID` int(25) NOT NULL,
  `Month` varchar(25) NOT NULL,
  `Services` varchar(25) NOT NULL,
  `Model` varchar(25) NOT NULL,
  `Unit` int(25) NOT NULL,
  `Invoice_Value` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `services_invoice`
--

INSERT INTO `services_invoice` (`Sr_No`, `Name_of_Company`, `Company_ID`, `Month`, `Services`, `Model`, `Unit`, `Invoice_Value`) VALUES
(1, 'Pape Audio', 1001, 'January', 'NEEM', 'A', 1500, 75000),
(2, 'Pape Audio', 1001, 'January', 'EL', 'A', 1800, 90000),
(3, 'Pape Audio', 1001, 'January', 'NAPS', 'A', 1000, 50000),
(4, 'Amigo Hospitality', 1002, 'January', 'NEEM', 'A', 3300, 165000),
(5, 'RVC Logistics', 1003, 'January', 'EL', 'A', 4400, 220000),
(6, 'RVC Logistics', 1003, 'January', 'NAPS', 'A', 3200, 160000);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
