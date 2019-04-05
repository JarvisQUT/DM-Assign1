# dm_tools_datarepair.py
import numpy as np
import pandas as pd

def data_prep():
      # read the CaseStudyData dataset
      df = pd.read_csv('CaseStudyData.csv')
    
      # drop columns
      df = df.drop(['PurchaseID','PurchaseTimestamp','PurchaseDate','Color','WheelTypeID','MMRCurrentRetailRatio','PRIMEUNIT','AUCGUART','ForSale'], axis=1)
    
      # prep 'Auction'
      df['Auction'] = df['Auction'].replace(np.nan,'MANHEIM')

      # prep 'VaHYear'
      df['VehYear'] = df['VehYear'].replace(np.nan,2006.0)
    
      # prep 'Make'
      df['Make'] = df['Make'].replace(np.nan,"CHEVROLET")

      # prep 'Transmission'    
      df['Transmission'] = df['Transmission'].replace('Manual','MANUAL')
      df['Transmission'] = df['Transmission'].replace('?','AUTO')
      df['Transmission'] = df['Transmission'].replace(np.nan,'AUTO')
      df['Transmission'] = df['Transmission'].astype(str)


      # prep 'WheelType'
      df['WheelType'] = df['WheelType'].replace("?","Alloy")
      df['WheelType'] = df['WheelType'].replace(np.nan,"Alloy")
   
      # prep 'VehOdo'
      df['VehOdo'] = df['VehOdo'].replace('?', 0)
      df['VehOdo'] = df['VehOdo'].astype(float)
      mask = df['VehOdo'] < 1
      df.loc[mask, 'VehOdo'] = np.nan
      df['VehOdo'].fillna(df['VehOdo'].mean(), inplace=True)
    
      # prep 'Nationality'
      df['Nationality'] = df['Nationality'].replace(np.nan,"AMERICAN")
      df['Nationality'] = df['Nationality'].replace("?","AMERICAN")
      df['Nationality'] = df['Nationality'].replace("USA","AMERICAN")

    
      # prep 'Size'
      df['Size'] = df['Size'].replace(np.nan,"MEDIUM")
      df['Size'] = df['Size'].replace("?","MEDIUM")

      # prep 'TopThreeAmericanName'
      df['TopThreeAmericanName'] = df['TopThreeAmericanName'].replace(np.nan,"GM")
      df['TopThreeAmericanName'] = df['TopThreeAmericanName'].replace("?","GM")

      # prep 'MMRAcquisitionAuctionAveragePrice'
      df['MMRAcquisitionAuctionAveragePrice'] = df['MMRAcquisitionAuctionAveragePrice'].replace('?',0)
      df['MMRAcquisitionAuctionAveragePrice'] = df['MMRAcquisitionAuctionAveragePrice'].astype(float)
      mask = df['MMRAcquisitionAuctionAveragePrice'] < 1
      df.loc[mask, 'MMRAcquisitionAuctionAveragePrice'] = np.nan
      df['MMRAcquisitionAuctionAveragePrice'].fillna(df['MMRAcquisitionAuctionAveragePrice'].mean(), inplace=True)

       # prep 'MMRAcquisitionAuctionCleanPrice'
      df['MMRAcquisitionAuctionCleanPrice'] = df['MMRAcquisitionAuctionCleanPrice'].replace('?',0)
      df['MMRAcquisitionAuctionCleanPrice'] = df['MMRAcquisitionAuctionCleanPrice'].astype(float)
      mask = df['MMRAcquisitionAuctionCleanPrice'] < 1
      df.loc[mask, 'MMRAcquisitionAuctionCleanPrice'] = np.nan
      df['MMRAcquisitionAuctionCleanPrice'].fillna(df['MMRAcquisitionAuctionCleanPrice'].mean(), inplace=True)

      # prep 'MMRAcquisitionRetailAveragePrice'
      df['MMRAcquisitionRetailAveragePrice'] = df['MMRAcquisitionRetailAveragePrice'].replace('?',0)
      df['MMRAcquisitionRetailAveragePrice'] = df['MMRAcquisitionRetailAveragePrice'].astype(float)
      mask = df['MMRAcquisitionRetailAveragePrice'] < 1
      df.loc[mask, 'MMRAcquisitionRetailAveragePrice'] = np.nan
      df['MMRAcquisitionRetailAveragePrice'].fillna(df['MMRAcquisitionRetailAveragePrice'].mean(), inplace=True)

      # prep 'MMRAcquisitonRetailCleanPrice'
      df['MMRAcquisitonRetailCleanPrice'] = df['MMRAcquisitonRetailCleanPrice'].replace('?',0)
      df['MMRAcquisitonRetailCleanPrice'] = df['MMRAcquisitonRetailCleanPrice'].astype(float)
      mask = df['MMRAcquisitonRetailCleanPrice'] < 1
      df.loc[mask, 'MMRAcquisitonRetailCleanPrice'] = np.nan
      df['MMRAcquisitonRetailCleanPrice'].fillna(df['MMRAcquisitonRetailCleanPrice'].mean(), inplace=True)

      # prep 'MMRCurrentAuctionAveragePrice'
      df['MMRCurrentAuctionAveragePrice'] = df['MMRCurrentAuctionAveragePrice'].replace('?',0)
      df['MMRCurrentAuctionAveragePrice'] = df['MMRCurrentAuctionAveragePrice'].astype(float)
      mask = df['MMRCurrentAuctionAveragePrice'] < 1
      df.loc[mask, 'MMRCurrentAuctionAveragePrice'] = np.nan
      df['MMRCurrentAuctionAveragePrice'].fillna(df['MMRCurrentAuctionAveragePrice'].mean(), inplace=True)

      # prep 'MMRCurrentAuctionCleanPrice'
      df['MMRCurrentAuctionCleanPrice'] = df['MMRCurrentAuctionCleanPrice'].replace('?',0)
      df['MMRCurrentAuctionCleanPrice'] = df['MMRCurrentAuctionCleanPrice'].astype(float)
      mask = df['MMRCurrentAuctionCleanPrice'] < 1
      df.loc[mask, 'MMRCurrentAuctionCleanPrice'] = np.nan
      df['MMRCurrentAuctionCleanPrice'].fillna(df['MMRCurrentAuctionCleanPrice'].mean(), inplace=True)

      # prep 'MMRCurrentRetailAveragePrice'
      df['MMRCurrentRetailAveragePrice'] = df['MMRCurrentRetailAveragePrice'].replace('?',0)
      df['MMRCurrentRetailAveragePrice'] = df['MMRCurrentRetailAveragePrice'].astype(float)
      mask = df['MMRCurrentRetailAveragePrice'] < 1
      df.loc[mask, 'MMRCurrentRetailAveragePrice'] = np.nan
      df['MMRCurrentRetailAveragePrice'].fillna(df['MMRCurrentRetailAveragePrice'].mean(), inplace=True)
   
      # prep 'MMRCurrentRetailCleanPrice'
      df['MMRCurrentRetailCleanPrice'] = df['MMRCurrentRetailCleanPrice'].replace('?',0)
      df['MMRCurrentRetailCleanPrice'] = df['MMRCurrentRetailCleanPrice'].astype(float)
      mask = df['MMRCurrentRetailCleanPrice'] < 1
      df.loc[mask, 'MMRCurrentRetailCleanPrice'] = np.nan
      df['MMRCurrentRetailCleanPrice'].fillna(df['MMRCurrentRetailCleanPrice'].mean(), inplace=True)
    
      # prep 'VNST'
      df['VNST'] = df['VNST'].replace(np.nan,"TX")

      # prep 'VehBCost'
      df['VehBCost'] = df['VehBCost'].replace('?',0)
      df['VehBCost'] = df['VehBCost'].astype(float)
      mask = df['VehBCost'] < 1
      df.loc[mask, 'VehBCost'] = np.nan
      df['VehBCost'].fillna(df['VehBCost'].mean(), inplace=True)

      # prep 'IsOnlineSale'
      df['IsOnlineSale'] = df['IsOnlineSale'].replace(1.0,1)
      df['IsOnlineSale'] = df['IsOnlineSale'].replace(-1.0,1)
      df['IsOnlineSale'] = df['IsOnlineSale'].replace(0.0,0)
      df['IsOnlineSale'] = df['IsOnlineSale'].replace("?",0)
      df['IsOnlineSale'] = df['IsOnlineSale'].replace(4.0,0)
      df['IsOnlineSale'] = df['IsOnlineSale'].replace(2.0,0)
      df['IsOnlineSale'] = df['IsOnlineSale'].replace(np.nan,0)
      df['IsOnlineSale'] = df['IsOnlineSale'].astype(int)
    
      # prep 'WarrantyCost'
      df.loc[mask, 'WarrantyCost'] = np.nan
      df['WarrantyCost'].fillna(df['WarrantyCost'].mean(), inplace=True)

      df = pd.get_dummies(df)    

      return df

### we can import it like this for the remaining of the practicals
# from dm_tools import data_prep