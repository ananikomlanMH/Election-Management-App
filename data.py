import pymysql as DB
from datetime import date
cn= DB.connect(host="localhost",user="root",database="election2016",password="")
cr = cn.cursor()
class Partis:

    #partis
    def add(self,nomParti):
        cr.execute("INSERT INTO parti (nomParti) VALUES (%s)",(nomParti))
        cn.commit()
        pass

    def edit(self,numParti, nomParti):
        cr.execute("UPDATE parti SET nomParti = %s WHERE numParti = %s",(nomParti, numParti))
        cn.commit()
        pass

    def delete(self,id):
        cr.execute("DELETE FROM parti WHERE numParti = %s",(id))
        cn.commit()
        pass

    def getAllParti(self,limit, sortData, dirData, page = 1, researchQuery = ''):
        cr.execute("SELECT * FROM parti WHERE nomParti LIKE CONCAT('%%', %s, '%%') ORDER BY " + sortData + " " + dirData +" LIMIT %s OFFSET %s",(researchQuery,limit,(limit*(int(page)-1))))
        return cr.fetchall()
        pass

    def getAllPartiforSearch(self):
        cr.execute("SELECT * FROM parti order by nomParti ASC")
        return cr.fetchall()
        pass
    
    def allVotePartis(self):
        cr.execute("SELECT * FROM pourcentage_parti_valable")
        result = cr.fetchall()
        data = {}
        for item in result:
            data[item[1]] = item[0]
        return data
    
    def voteWinner(self):
        cr.execute("SELECT * FROM pourcentage_parti_valable ORDER BY voix DESC LIMIT 1")
        return cr.fetchone()

    def getCountParti(self, researchQuery = ''):
        cr.execute("SELECT COUNT(*) FROM parti WHERE nomParti LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        return cr.fetchone()[0]
        pass

class Regions:

    #regions
    def add(self,region):
        cr.execute("INSERT INTO region (region) VALUES (%s)",(region))
        cn.commit()
        pass

    def edit(self,numRegion, region):
        cr.execute("UPDATE region SET region = %s WHERE numRegion = %s",(region, numRegion))
        cn.commit()
        pass

    def delete(self,id):
        cr.execute("DELETE FROM region WHERE numRegion = %s",(id))
        cn.commit()
        pass

    def getAllRegion(self,limit, sortData, dirData, page = 1, researchQuery = ''):
        cr.execute("SELECT * FROM region WHERE region LIKE CONCAT('%%', %s, '%%') ORDER BY " + sortData + " " + dirData +" LIMIT %s OFFSET %s",(researchQuery,limit,(limit*(int(page)-1))))
        return cr.fetchall()
        pass

    def getAllRegionforSearch(self):
        cr.execute("SELECT * FROM region order by region ASC")
        return cr.fetchall()
        pass

    def allVote(self):
        cr.execute("SELECT * FROM pourcentage_region")
        result = cr.fetchall()
        data = {}
        for item in result:
            data[item[1]] = item[0]
        return data

    def allVoteTous(self):
        cr.execute("SELECT * FROM pourcentage_region_all")
        result = cr.fetchall()
        data = {}
        for item in result:
            data[item[1]] = item[0]
        return data

    def allVoteBlanc(self):
        cr.execute("SELECT * FROM pourcentage_region_blanc")
        result = cr.fetchall()
        data = {}
        for item in result:
            data[item[1]] = item[0]
        return data

    def allVotePresi(self):
        cr.execute("SELECT * FROM pourcentage_region_presidentielles")
        result = cr.fetchall()
        data = []
        for item in result:
            data.append(item[0])
        return data

    def allVoteLegi(self):
        cr.execute("SELECT * FROM pourcentage_region_legislatives")
        result = cr.fetchall()
        data = []
        for item in result:
            data.append(item[0])
        return data

    def allVoteAll(self):
        cr.execute("SELECT * FROM pourcentage_region_typevote")
        data = []
        result = cr.fetchall()
        data = []
        for item in result:
            data.append(item[0])
        return data

    def getCountRegion(self, researchQuery = ''):
        cr.execute("SELECT COUNT(*) FROM region WHERE region LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        return cr.fetchone()[0]
        pass

class Departements:

    #Departements
    def add(self,departement,REGION_numRegion):
        cr.execute("INSERT INTO departement (departement,REGION_numRegion) VALUES (%s,%s)",(departement,REGION_numRegion))
        cn.commit()
        pass

    def edit(self,numDepartement,departement,REGION_numRegion):
        cr.execute("UPDATE departement SET departement = %s , REGION_numRegion = %s WHERE numDepartement = %s",(departement,REGION_numRegion,numDepartement))
        cn.commit()
        pass

    def delete(self,numDepartement):
        cr.execute("DELETE FROM departement WHERE numDepartement = %s",(numDepartement))
        cn.commit()
        pass

    def getAllDepartement(self,limit, sortData, dirData, page = 1, researchQuery = ''):
        cr.execute("SELECT departement.departement, region.region, departement.REGION_numRegion, departement.numDepartement FROM departement, region WHERE region.numRegion = departement.REGION_numRegion AND departement.departement LIKE CONCAT('%%', %s, '%%') ORDER BY " + sortData + " " + dirData +" LIMIT %s OFFSET %s",(researchQuery,limit,(limit*(int(page)-1))))
        return cr.fetchall()
        pass

    def getAllDepartementforSearch(self):
        cr.execute("SELECT * FROM departement order by departement ASC")
        return cr.fetchall()
        pass

    def getCountDepartement(self, researchQuery = ''):
        cr.execute("SELECT COUNT(*) FROM departement WHERE departement LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        return cr.fetchone()[0]
        pass

class Communes:

    #Communes
    def add(self,commune,DEPARTEMENT_numDepartement):
        cr.execute("INSERT INTO commune (commune,DEPARTEMENT_numDepartement) VALUES (%s,%s)",(commune,DEPARTEMENT_numDepartement))
        cn.commit()
        pass

    def edit(self,numCommune,commune,DEPARTEMENT_numDepartement):
        cr.execute("UPDATE commune SET commune = %s , DEPARTEMENT_numDepartement = %s WHERE numCommune = %s",(commune,DEPARTEMENT_numDepartement,numCommune))
        cn.commit()
        pass

    def delete(self,numCommune):
        cr.execute("DELETE FROM commune WHERE numCommune = %s",(numCommune))
        cn.commit()
        pass

    def getAllCommune(self,limit, sortData, dirData, page = 1, researchQuery = ''):
        cr.execute("SELECT commune.commune, departement.departement, commune.numCommune, commune.DEPARTEMENT_numDepartement FROM commune, departement WHERE departement.numDepartement = commune.DEPARTEMENT_numDepartement AND commune.commune LIKE CONCAT('%%', %s, '%%') ORDER BY " + sortData + " " + dirData +" LIMIT %s OFFSET %s",(researchQuery,limit,(limit*(int(page)-1))))
        return cr.fetchall()
        pass

    def getAllCommuneforSearch(self):
        cr.execute("SELECT * FROM commune order by commune ASC")
        return cr.fetchall()
        pass

    def getCountCommune(self, researchQuery = ''):
        cr.execute("SELECT COUNT(*) FROM commune WHERE commune LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        return cr.fetchone()[0]
        pass

class Bureau:

    #Bureau
    def add(self,COMMUNE_numCommue):
        cr.execute("INSERT INTO bureau (COMMUNE_numCommue) VALUES (%s)",(COMMUNE_numCommue))
        cn.commit()
        pass

    def edit(self,numBureau,COMMUNE_numCommue):
        cr.execute("UPDATE bureau SET COMMUNE_numCommue = %s  WHERE numBureau = %s",(COMMUNE_numCommue,numBureau))
        cn.commit()
        pass

    def delete(self,numBureau):
        cr.execute("DELETE FROM bureau WHERE numBureau = %s",(numBureau))
        cn.commit()
        pass

    def getAllBureau(self,limit, sortData, dirData, page = 1, researchQuery = ''):
        cr.execute("SELECT bureau.numBureau, commune.commune, bureau.COMMUNE_numCommue FROM bureau, commune WHERE bureau.COMMUNE_numCommue = commune.numCommune AND bureau.numBureau LIKE CONCAT('%%', %s, '%%') ORDER BY " + sortData + " " + dirData +" LIMIT %s OFFSET %s",(researchQuery,limit,(limit*(int(page)-1))))
        return cr.fetchall()
        pass

    def getAllBureauforSearch(self):
        cr.execute("SELECT * FROM bureau order by numBureau ASC")
        return cr.fetchall()
        pass

    def getCountBureau(self, researchQuery = ''):
        cr.execute("SELECT COUNT(*) FROM bureau WHERE numBureau LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        return cr.fetchone()[0]
        pass

class Candidats:

    #Bureau
    def add(self,nomCandidat,prenomCandidat,date_naissCandidat,lieuNaissCandidat,genreCandidat,TYPECANDIDAT_idType,PARTI_numParti):
        cr.execute('''INSERT INTO candidat (nomCandidat,prenomCandidat,date_naissCandidat,lieuNaissCandidat,genreCandidat,TYPECANDIDAT_idType,PARTI_numParti) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)''',(nomCandidat,prenomCandidat,date_naissCandidat,lieuNaissCandidat,genreCandidat,TYPECANDIDAT_idType,PARTI_numParti))
        cn.commit()
        pass

    def edit(self,nomCandidat,prenomCandidat,date_naissCandidat,lieuNaissCandidat,genreCandidat,TYPECANDIDAT_idType,PARTI_numParti, numCandidat):
        cr.execute('''UPDATE candidat SET nomCandidat = %s ,prenomCandidat = %s ,date_naissCandidat = %s ,lieuNaissCandidat = %s ,genreCandidat = %s ,
        TYPECANDIDAT_idType = %s ,PARTI_numParti = %s WHERE numCandidat = %s''',(nomCandidat,prenomCandidat,date_naissCandidat,lieuNaissCandidat,genreCandidat,TYPECANDIDAT_idType,PARTI_numParti,numCandidat))
        cn.commit()
        pass

    def delete(self,numCandidat):
        cr.execute("DELETE FROM candidat WHERE numCandidat = %s",(numCandidat))
        cn.commit()
        pass

    def getAllCandidat(self,limit,typeCandidat, sortData, dirData, page = 1, researchQuery = ''):
        if (typeCandidat == 'all'):
            cr.execute('''SELECT candidat.numCandidat, candidat.nomCandidat, candidat.prenomCandidat,  
            candidat.date_naissCandidat, candidat.lieuNaissCandidat, candidat.genreCandidat, candidat.TYPECANDIDAT_idType,
            candidat.PARTI_numParti, typecandidat.type , parti.nomParti FROM candidat, typecandidat, parti
            WHERE candidat.TYPECANDIDAT_idType = typecandidat.idType AND candidat.PARTI_numParti = parti.numParti AND CONCAT(nomCandidat, ' ',prenomCandidat) LIKE CONCAT('%%', %s, '%%') 
            ORDER BY '''+ sortData + " " + dirData +''' LIMIT %s OFFSET %s''',(researchQuery,limit,(limit*(int(page)-1))))
        elif (typeCandidat == '1'):
            cr.execute('''SELECT candidat.numCandidat, candidat.nomCandidat, candidat.prenomCandidat,  
            candidat.date_naissCandidat, candidat.lieuNaissCandidat, candidat.genreCandidat, candidat.TYPECANDIDAT_idType,
            candidat.PARTI_numParti, typecandidat.type , parti.nomParti FROM candidat, typecandidat, parti
            WHERE candidat.TYPECANDIDAT_idType = typecandidat.idType AND candidat.PARTI_numParti = parti.numParti AND candidat.TYPECANDIDAT_idType = '2' 
            AND CONCAT(nomCandidat, ' ',prenomCandidat) LIKE CONCAT('%%', %s, '%%') 
            ORDER BY ''' + sortData + " " + dirData +''' LIMIT %s OFFSET %s''',(researchQuery,limit,(limit*(int(page)-1))))
        elif (typeCandidat == '0'):
            cr.execute('''SELECT candidat.numCandidat, candidat.nomCandidat, candidat.prenomCandidat,  
            candidat.date_naissCandidat, candidat.lieuNaissCandidat, candidat.genreCandidat, candidat.TYPECANDIDAT_idType,
            candidat.PARTI_numParti, typecandidat.type , parti.nomParti FROM candidat, typecandidat, parti
            WHERE candidat.TYPECANDIDAT_idType = typecandidat.idType AND candidat.PARTI_numParti = parti.numParti 
            AND candidat.TYPECANDIDAT_idType = '1' AND CONCAT(nomCandidat, ' ',prenomCandidat) LIKE CONCAT('%%', %s, '%%') 
            ORDER BY ''' + sortData + " " + dirData +''' LIMIT %s OFFSET %s''',(researchQuery,limit,(limit*(int(page)-1))))
        return cr.fetchall()
        pass

    def getAllCandidatforSearch(self):
        cr.execute("SELECT * FROM candidat order by nomCandidat ASC")
        return cr.fetchall()
        pass

    def getAllType(self):
        cr.execute("SELECT * FROM typecandidat order by type ASC")
        return cr.fetchall()
        pass

    def getCountCandidat(self,typeCandidat, researchQuery = ''):
        if (typeCandidat == 'all'):
            cr.execute("SELECT COUNT(*) FROM candidat WHERE CONCAT(nomCandidat, ' ',prenomCandidat) LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        elif (typeCandidat == '1'):
            cr.execute("SELECT COUNT(*) FROM candidat WHERE TYPECANDIDAT_idType = '2' AND CONCAT(nomCandidat, ' ',prenomCandidat) LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        elif (typeCandidat == '0'):
            cr.execute("SELECT COUNT(*) FROM candidat WHERE TYPECANDIDAT_idType = '1' AND CONCAT(nomCandidat, ' ',prenomCandidat) LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        return cr.fetchone()[0]
        pass

class Electeur:

    #electeur
    def add(self,nomElecteur,prenomElecteur,dateNaissElecteur,genreElecteur,numPiece,numBureau):
        cr.execute('''INSERT INTO electeur (nomElecteur,prenomElecteur,dateNaissElecteur,genreElecteur,numPiece) 
        VALUES (%s,%s,%s,%s,%s)''',(nomElecteur,prenomElecteur,dateNaissElecteur,genreElecteur,numPiece))
        cn.commit()
        cr.execute("SELECT numElecteur FROM electeur ORDER BY numElecteur DESC LIMIT 1")
        idElecteur = cr.fetchone()[0]
        cr.execute("INSERT INTO inscrire (numBureau,numElecteur) values (%s,%s)",(numBureau,idElecteur))
        cn.commit()
        pass

    def edit(self,numElecteur,nomElecteur,prenomElecteur,dateNaissElecteur,genreElecteur,numPiece,numBureau):
        cr.execute("UPDATE electeur SET nomElecteur = %s ,prenomElecteur = %s ,dateNaissElecteur = %s,genreElecteur = %s ,numPiece = %s WHERE numElecteur = %s",(nomElecteur,prenomElecteur,dateNaissElecteur,genreElecteur,numPiece,numElecteur))
        cn.commit()

        cr.execute("UPDATE inscrire SET numBureau = %s WHERE numElecteur = %s",(numBureau,numElecteur))
        cn.commit()

    def delete(self,numElecteur):
        cr.execute("DELETE FROM inscrire WHERE numElecteur = %s",(numElecteur))
        cn.commit()
        cr.execute("DELETE FROM electeur WHERE numElecteur = %s",(numElecteur))
        cn.commit()
        pass

    def getAllElecteur(self,limit, sortData, dirData, page = 1, researchQuery = ''):
        cr.execute('''SELECT electeur.numElecteur,electeur.nomElecteur,electeur.prenomElecteur,electeur.dateNaissElecteur,
        electeur.genreElecteur,electeur.numPiece, inscrire.numBureau, inscrire.numElecteur, bureau.numBureau FROM electeur, bureau, inscrire
        WHERE inscrire.numBureau = bureau.numBureau AND inscrire.numElecteur = electeur.numElecteur
        AND CONCAT(electeur.nomElecteur, ' ',electeur.prenomElecteur) LIKE CONCAT('%%', %s, '%%') ORDER BY ''' + sortData + ''' ''' + dirData +''' LIMIT %s OFFSET %s''',(researchQuery,limit,(limit*(int(page)-1))))
        return cr.fetchall()
        pass

    def getAllElecteurforSearch(self):
        cr.execute("SELECT * FROM electeur order by nomElecteur ASC")
        return cr.fetchall()
        pass

    def getCountElecteur(self, researchQuery = ''):
        cr.execute("SELECT COUNT(*) FROM electeur WHERE CONCAT(nomElecteur, ' ',prenomElecteur) LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        return cr.fetchone()[0]
        pass

class Voter:

    #Voter
    def add(self,numCandidat,numElecteur,BUREAU_numBureau,Voix,Procuration,typeVote):

        cr.execute('''SELECT COUNT(*) FROM voter where numElecteur = %s''',(numElecteur))
        nbr = cr.fetchone()[0]
        if int(nbr) > 0:
            return False;
        else:
            cr.execute('''INSERT INTO voter VALUES (%s,%s,%s,%s,%s,%s,%s)''',(numCandidat,numElecteur,BUREAU_numBureau,Voix,date.today(),Procuration,typeVote))
            cn.commit()
            return True;

    def getAllVote(self,limit,voix,proc,typeVote, sortData, dirData, page = 1, researchQuery = ''):
        sql = '''SELECT electeur.nomElecteur,electeur.prenomElecteur ,
            candidat.nomCandidat, candidat.prenomCandidat, voter.BUREAU_numBureau, voter.voix, voter.jour, voter.Procuration, voter.typeVote
            FROM electeur, voter, candidat, bureau
            WHERE electeur.numElecteur = voter.numElecteur AND candidat.numCandidat = voter.numCandidat AND 
            bureau.numBureau = voter.BUREAU_numBureau '''

        if voix == 'all' or proc == 'all' or typeVote == 'all':
            sql += ''
        
        if voix == '1':
            sql += 'AND voix = 1 '

        if voix == '0':
            sql += 'AND voix = 0 '
        
        if proc == '1':
            sql += 'AND Procuration = 1 '

        if proc == '0':
            sql += 'AND Procuration = 0 '
        
        if typeVote == '1':
            sql += 'AND typeVote = 1 '

        if typeVote == '0':
            sql += 'AND typeVote = 0 '

        cr.execute(sql+" AND CONCAT(nomCandidat, ' ',prenomCandidat) LIKE CONCAT('%%', %s, '%%') ORDER BY " + sortData + " " + dirData +" LIMIT %s OFFSET %s",(researchQuery,limit,(limit*(int(page)-1))))
        return cr.fetchall()

    def getAllVoteforSearch(self):
        cr.execute("SELECT * FROM candidat order by numCandidat ASC")
        return cr.fetchall()
        pass

    def getCountVote(self,voix,proc,typeVote, researchQuery = ''):
        sql = '''SELECT COUNT(*) FROM electeur, voter, candidat, bureau WHERE electeur.numElecteur = voter.numElecteur AND candidat.numCandidat = voter.numCandidat AND 
        bureau.numBureau = voter.BUREAU_numBureau '''

        if voix == 'all' or proc == 'all' or typeVote == 'all':
            sql += ''
        
        if voix == '1':
            sql += 'AND voix = 1 '

        if voix == '0':
            sql += 'AND voix = 0 '
        
        if proc == '1':
            sql += 'AND Procuration = 1 '

        if proc == '0':
            sql += 'AND Procuration = 0 '
        
        if typeVote == '1':
            sql += 'AND typeVote = 1 '

        if typeVote == '0':
            sql += 'AND typeVote = 0 '

        cr.execute(sql+" AND CONCAT(candidat.nomCandidat, ' ',candidat.prenomCandidat) LIKE CONCAT('%%', %s, '%%')",(researchQuery))
        return cr.fetchone()[0]
        pass
