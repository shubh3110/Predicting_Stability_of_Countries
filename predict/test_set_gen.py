import pandas as pd
import numpy as np

k=17
while(k<=18):
    if(k<10):
        df=pd.read_csv('fsi/fsi-200'+str(k)+'.csv')
        temp=df.drop(df.columns[4:],axis=1)
        temp.rename(columns={'Total':'Fsi Score'},inplace=True)
    else:
        df=pd.read_csv('fsi/fsi-20'+str(k)+'.csv')
        temp=df.drop(df.columns[4:],axis=1)
        temp.rename(columns={'Total':'Fsi Score'},inplace=True)
    
    df1=pd.read_csv('debt/debt_final.csv')
    debt=[]
    i=0
    l=len(temp)-1
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    debt.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    debt.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            debt.append(0)
        i+=1

    temp['Debt']=debt

    df1=pd.read_csv('environment/environment_final.csv')
    environment=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    environment.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    environment.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            environment.append(0)
        i+=1
        
    temp['Environment']=environment

    df1=pd.read_csv('financial sector/financial sector_final.csv')
    financial_sector=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    financial_sector.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    financial_sector.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            financial_sector.append(0)
        i+=1
        
    temp['Financial Sector']=financial_sector
    
    df1=pd.read_csv('health/health_final.csv')
    health=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    health.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    health.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            health.append(0)
        i+=1
        
    temp['Health']=health
    
    df1=pd.read_csv('infrastructure/infrastructure_final.csv')
    infrastructure=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    infrastructure.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    infrastructure.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            infrastructure.append(0)
        i+=1
        
    temp['Infrastructure']=infrastructure

    df1=pd.read_csv('labour/labour_final.csv')
    labour=[]
    i=0
    cnt=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    labour.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    labour.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            labour.append(0)
            cnt+=1
        i+=1
        
    temp['Labour']=labour
            
    df1=pd.read_csv('poverty/poverty_final.csv')
    poverty=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    poverty.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    poverty.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            poverty.append(0)
        i+=1
        
    temp['Poverty']=poverty

    df1=pd.read_csv('private sector/private sector_final.csv')
    private_sector=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    private_sector.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    private_sector.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            private_sector.append(0)
        i+=1
        
    temp['Private Sector']=private_sector

    df1=pd.read_csv('public sector/public sector_final.csv')
    public_sector=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    public_sector.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    public_sector.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            public_sector.append(0)
        i+=1
        
    temp['Public Sector']=public_sector
    
    df1=pd.read_csv('social protection/social protection_final.csv')
    social_protection=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    social_protection.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    social_protection.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            social_protection.append(0)
        i+=1
        
    temp['Social Protection']=social_protection

    df1=pd.read_csv('trade/trade_final.csv')
    trade=[]
    i=0
    while(i<=l):
        j=0
        flag=0
        while(j<=263):
            if(temp['Country'][i]==df1['Country Name'][j]):
                if(k<10):
                    trade.append(df1['200'+str(k)+' [YR200'+str(k)+']'][j])
                    flag=1
                    break
                else:
                    trade.append(df1['20'+str(k)+' [YR20'+str(k)+']'][j])
                    flag=1
                    break
            j+=1
        if(flag==0):
            trade.append(0)
        i+=1
        
    temp['Trade']=trade

    #loading from dataframe to csv
    if(k<10):
        temp.to_csv('fsi_200'+str(k)+'_final.csv',encoding='utf-8', index=False)
    else:
        temp.to_csv('fsi_20'+str(k)+'_final.csv',encoding='utf-8', index=False)
    k+=1


df=pd.read_csv('fsi_2017_final.csv')
df

temp=pd.read_csv('fsi_2018_final.csv')
temp

df=pd.concat([df,temp],axis=0)
df

result=df.drop(df.columns[4:],axis=1)
result

result.drop(['Rank'],axis=1,inplace=True)
result

#loading from dataframe to csv
result.to_csv('result.csv',encoding='utf-8', index=False)
result.dtypes

df.drop(['Rank','Fsi Score'],axis=1,inplace=True)
df

test=df
test

#loading from dataframe to csv
test.to_csv('test.csv',encoding='utf-8', index=False)
test.dtypes

