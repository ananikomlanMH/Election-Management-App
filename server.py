from math import ceil
from re import I
import urllib.parse
from flask import Flask, flash,render_template,redirect,request,session,url_for, jsonify
from data import Partis, Regions , Departements, Communes, Bureau, Candidats, Electeur, Voter
PER_PAGE = 11

app=Flask(__name__)
app.config['SECRET_KEY'] = "ma super cle"

def urlHelper(param, value):
    urlBase = request.args
    url2 = dict(urlBase.copy())
    params = [(param, value)]
    url2.update(params)
    return urllib.parse.urlencode(url2)

def urlHelperWiths2Params(param1, value1, param2, value2):
    urlBase = request.args
    url2 = dict(urlBase.copy())
    params = [(param1, value1),(param2, value2)]
    url2.update(params)
    return urllib.parse.urlencode(url2)

def th(key, sort, title):
    sortKey = request.args.get('sort','') if(request.args.get('sort','')) else None
    dirKey = request.args.get('dir','') if(request.args.get('dir','')) else None
    if(dirKey is not None and sortKey == key):
        icon = '<i class="fi fi-rr-angle-small-up"></i>' if(dirKey == 'ASC') else '<i class="fi fi-rr-angle-small-down"></i>'
    else:
        icon = ''

    url = urlHelperWiths2Params('sort', key, 'dir' , 'DESC' if(dirKey == 'ASC' and sortKey == key) else 'ASC')
    return "<a href=\"?"+url+"\">"+title + icon+"</a>"

app.jinja_env.globals.update(urlHelper = urlHelper, urlHelperWiths2Params = urlHelperWiths2Params, th = th)

@app.route('/')
def index():
   return redirect(url_for('login'))

@app.route('/dashboard/')
def dashboard():
    allCandidat = Candidats().getCountCandidat('all','')
    allElecteur = Electeur().getCountElecteur('')
    allParti = Partis().getCountParti('')
    allBureau = Bureau().getCountBureau('')
    votePresi = Regions().allVotePresi()
    voteLegis = Regions().allVoteLegi()
    allVoteAll = Regions().allVoteAll()
    return render_template('dashboard.html',activate='dashboard',allVoteAll = allVoteAll, voteLegis = voteLegis, votePresi = votePresi, allBureau = allBureau, allCandidat = allCandidat, allElecteur = allElecteur, allParti = allParti)

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/loginUser/', methods = ['POST'])
def loginUser():
   if request.method == 'POST':
      session['username'] = request.form['username']
      session['password'] = request.form['password']
      flash('Bienvenu '+session['username'],'success')
      return redirect(url_for('dashboard'))

@app.route('/logout/')
def logout():
   session.pop('username', None)
   session.pop('password', None)
   flash('Deconnecté avec succès','success')
   return redirect(url_for('login'))

# Gestion des regions
@app.route('/regions/')
def regions():

    if(request.args.get('p','')):
        currentPage = int(request.args.get('p',''))
    else:
        currentPage = 1

    if(request.args.get('show','')):
        limit = int(request.args.get('show',''))
    else:
        limit = PER_PAGE

    if(request.args.get('q','')):
        researchQuery = request.args.get('q','')
    else:
        researchQuery = ''

    if(request.args.get('sort','')):
        sortData = str(request.args.get('sort',''))
        dirData = str(request.args.get('dir',''))
    else:
        sortData = 'region'
        dirData = 'ASC'

    allRegion = Regions().getAllRegion(limit, sortData, dirData, currentPage, researchQuery)
    
    nbrElements = Regions().getCountRegion(researchQuery)
    
    nbrPage = ceil(nbrElements/limit)
    
    if(nbrElements > 1):
        nbr_elements_courant = (limit * (currentPage-1)) + int(len(allRegion))
    else:
        nbr_elements_courant = int(len(allRegion))
    
    searchFields = Regions().getAllRegionforSearch()
    search = []
    for item in searchFields:
        data = {"id":item[0],"value":item[1]}
        search.append(data)

    jsonSearch = search
    voteRegion = Regions().allVote()
    allVoteTous = Regions().allVoteTous()
    allVoteBlanc = Regions().allVoteBlanc()
    return render_template('region.html', activate='regions', jsonSearch = jsonSearch,allVoteTous = allVoteTous, allVoteBlanc= allVoteBlanc, voteRegion = voteRegion, allRegion = allRegion, nbrElements = nbrElements, nbrPage = nbrPage, currentPage = currentPage, nbr_elements_courant = nbr_elements_courant)

@app.route('/addRegion',methods=['POST'])
def addRegion():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            region = request.form['region']
            Regions().add(region)
    flash('Region ajouté','success')
    return redirect(url_for('regions'))

@app.route('/editRegion',methods=['POST'])
def editRegion():
    if request.method == 'POST':
        button = request.form['edit']
        if button == 'Enregistrer':
            region = request.form['region']
            numRegion = request.form['numRegion']
            Regions().edit(numRegion,region)
    flash('Region modifié','success')
    return redirect(url_for('regions'))

@app.route('/deleteRegion/<int:numRegion>')
def deleteRegion(numRegion):
    Regions().delete([numRegion])
    flash('Region supprimée','success')
    return redirect(url_for('regions'))

# Gestion des departements
@app.route('/departements/')
def departements():

    if(request.args.get('p','')):
        currentPage = int(request.args.get('p',''))
    else:
        currentPage = 1

    if(request.args.get('show','')):
        limit = int(request.args.get('show',''))
    else:
        limit = PER_PAGE

    if(request.args.get('q','')):
        researchQuery = request.args.get('q','')
    else:
        researchQuery = ''

    if(request.args.get('sort','')):
        sortData = str(request.args.get('sort',''))
        dirData = str(request.args.get('dir',''))
    else:
        sortData = 'departement'
        dirData = 'ASC'

    allDepartement = Departements().getAllDepartement(limit, sortData, dirData, currentPage, researchQuery)
    
    nbrElements = Departements().getCountDepartement(researchQuery)
    
    nbrPage = ceil(nbrElements/limit)
    
    if(nbrElements > 1):
        nbr_elements_courant = (limit * (currentPage-1)) + int(len(allDepartement))
    else:
        nbr_elements_courant = int(len(allDepartement))
    
    searchFields = Departements().getAllDepartementforSearch()
    search = []
    for item in searchFields:
        data = {"id":item[0],"value":item[1]}
        search.append(data)

    jsonSearch = search
    allRegion = Regions().getAllRegionforSearch()
    return render_template('departement.html', activate='departements', jsonSearch = jsonSearch, allDepartement = allDepartement, allRegion = allRegion, nbrElements = nbrElements, nbrPage = nbrPage, currentPage = currentPage, nbr_elements_courant = nbr_elements_courant)

@app.route('/addDepartement',methods=['POST'])
def addDepartement():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            departement = request.form['departement']
            region = request.form['REGION_numRegion']
            Departements().add(departement,region)
    flash('Departement ajouté','success')
    return redirect(url_for('departements'))

@app.route('/editDepartement',methods=['POST'])
def editDepartement():
    if request.method == 'POST':
        button = request.form['edit']
        if button == 'Enregistrer':
            numDepartement = request.form['numDepartement']
            departement = request.form['departement']
            region = request.form['REGION_numRegion']
            Departements().edit(numDepartement,departement,region)
    flash('Departement modifié','success')
    return redirect(url_for('departements'))

@app.route('/deleteDepartement/<int:numDepartement>')
def deleteDepartement(numDepartement):
    Departements().delete([numDepartement])
    flash('Departement supprimée','success')
    return redirect(url_for('departements'))

# Gestion des communes
@app.route('/communes/')
def communes():

    if(request.args.get('p','')):
        currentPage = int(request.args.get('p',''))
    else:
        currentPage = 1

    if(request.args.get('show','')):
        limit = int(request.args.get('show',''))
    else:
        limit = PER_PAGE

    if(request.args.get('q','')):
        researchQuery = request.args.get('q','')
    else:
        researchQuery = ''

    if(request.args.get('sort','')):
        sortData = str(request.args.get('sort',''))
        dirData = str(request.args.get('dir',''))
    else:
        sortData = 'commune'
        dirData = 'ASC'

    allCommune = Communes().getAllCommune(limit, sortData, dirData, currentPage, researchQuery)
    
    nbrElements = Communes().getCountCommune(researchQuery)
    
    nbrPage = ceil(nbrElements/limit)
    
    if(nbrElements > 1):
        nbr_elements_courant = (limit * (currentPage-1)) + int(len(allCommune))
    else:
        nbr_elements_courant = int(len(allCommune))
    
    searchFields = Communes().getAllCommuneforSearch()
    search = []
    for item in searchFields:
        data = {"id":item[0],"value":item[1]}
        search.append(data)

    jsonSearch = search
    allDepartement = Departements().getAllDepartementforSearch()
    return render_template('commune.html', activate='communes', jsonSearch = jsonSearch, allCommune = allCommune, allDepartement = allDepartement, nbrElements = nbrElements, nbrPage = nbrPage, currentPage = currentPage, nbr_elements_courant = nbr_elements_courant)

@app.route('/addCommune',methods=['POST'])
def addCommune():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            commune = request.form['commune']
            departement = request.form['DEPARTEMENT_numDepartement']
            Communes().add(commune,departement)
    flash('Commune ajouté','success')
    return redirect(url_for('communes'))

@app.route('/editCommune',methods=['POST'])
def editCommune():
    if request.method == 'POST':
        button = request.form['edit']
        if button == 'Enregistrer':
            numCommune = request.form['numCommune']
            commune = request.form['commune']
            departement = request.form['DEPARTEMENT_numDepartement']
            Communes().edit(numCommune,commune,departement)
    flash('Commune modifié','success')
    return redirect(url_for('communes'))

@app.route('/deleteCommune/<int:numCommune>')
def deleteCommune(numCommune):
    Communes().delete([numCommune])
    flash('Commune supprimée','success')
    return redirect(url_for('communes'))

# Gestion des bureau
@app.route('/bureau/')
def bureau():

    if(request.args.get('p','')):
        currentPage = int(request.args.get('p',''))
    else:
        currentPage = 1

    if(request.args.get('show','')):
        limit = int(request.args.get('show',''))
    else:
        limit = PER_PAGE

    if(request.args.get('q','')):
        researchQuery = request.args.get('q','')
    else:
        researchQuery = ''

    if(request.args.get('sort','')):
        sortData = str(request.args.get('sort',''))
        dirData = str(request.args.get('dir',''))
    else:
        sortData = 'numBureau'
        dirData = 'ASC'

    allBureau = Bureau().getAllBureau(limit, sortData, dirData, currentPage, researchQuery)
    
    nbrElements = Bureau().getCountBureau(researchQuery)
    
    nbrPage = ceil(nbrElements/limit)
    
    if(nbrElements > 1):
        nbr_elements_courant = (limit * (currentPage-1)) + int(len(allBureau))
    else:
        nbr_elements_courant = int(len(allBureau))
    
    searchFields = Bureau().getAllBureauforSearch()
    search = []
    for item in searchFields:
        data = {"id":item[0],"value":item[1]}
        search.append(data)

    jsonSearch = search
    allCommune = Communes().getAllCommuneforSearch()
    return render_template('bureau.html', activate='bureau', jsonSearch = jsonSearch, allBureau = allBureau, allCommune = allCommune, nbrElements = nbrElements, nbrPage = nbrPage, currentPage = currentPage, nbr_elements_courant = nbr_elements_courant)

@app.route('/addBureau',methods=['POST'])
def addBureau():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            commune = request.form['COMMUNE_numCommue']
            Bureau().add(commune)
    flash('Bureau ajouté','success')
    return redirect(url_for('bureau'))

@app.route('/editBureau',methods=['POST'])
def editBureau():
    if request.method == 'POST':
        button = request.form['edit']
        if button == 'Enregistrer':
            numBureau = request.form['numBureau']
            commune = request.form['COMMUNE_numCommue']
            Bureau().edit(numBureau,commune)
    flash('Bureau modifié','success')
    return redirect(url_for('bureau'))

@app.route('/deleteBureau/<int:numBureau>')
def deleteBureau(numBureau):
    Bureau().delete([numBureau])
    flash('Bureau supprimée','success')
    return redirect(url_for('bureau'))

# Gestion des partis
@app.route('/partis/')
def partis():

    if(request.args.get('p','')):
        currentPage = int(request.args.get('p',''))
    else:
        currentPage = 1

    if(request.args.get('show','')):
        limit = int(request.args.get('show',''))
    else:
        limit = PER_PAGE

    if(request.args.get('q','')):
        researchQuery = request.args.get('q','')
    else:
        researchQuery = ''

    if(request.args.get('sort','')):
        sortData = str(request.args.get('sort',''))
        dirData = str(request.args.get('dir',''))
    else:
        sortData = 'nomParti'
        dirData = 'ASC'

    allParti = Partis().getAllParti(limit, sortData, dirData, currentPage, researchQuery)
    
    nbrElements = Partis().getCountParti(researchQuery)
    
    nbrPage = ceil(nbrElements/limit)
    
    if(nbrElements > 1):
        nbr_elements_courant = (limit * (currentPage-1)) + int(len(allParti))
    else:
        nbr_elements_courant = int(len(allParti))
    
    searchFields = Partis().getAllPartiforSearch()
    search = []
    for item in searchFields:
        data = {"id":item[0],"value":item[1]}
        search.append(data)

    jsonSearch = search

    allVotePartis = Partis().allVotePartis()
    voteWinner = Partis().voteWinner()
    return render_template('parti.html', activate='partis',voteWinner = voteWinner,allVotePartis = allVotePartis, jsonSearch = jsonSearch, allParti = allParti, nbrElements = nbrElements, nbrPage = nbrPage, currentPage = currentPage, nbr_elements_courant = nbr_elements_courant)

@app.route('/addParti',methods=['POST'])
def addParti():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            parti = request.form['nomParti']
            Partis().add(parti)
    flash('Parti ajouté','success')
    return redirect(url_for('partis'))

@app.route('/editParti',methods=['POST'])
def editParti():
    if request.method == 'POST':
        button = request.form['edit']
        if button == 'Enregistrer':
            parti = request.form['nomParti']
            numParti = request.form['numParti']
            Partis().edit(numParti,parti)
    flash('Parti modifié','success')
    return redirect(url_for('partis'))

@app.route('/deleteParti/<int:numParti>')
def deleteParti(numParti):
    Partis().delete([numParti])
    flash('Parti supprimée','success')
    return redirect(url_for('partis'))


# Gestion des candidats
@app.route('/candidats/')
def candidats():

    if(request.args.get('p','')):
        currentPage = int(request.args.get('p',''))
    else:
        currentPage = 1

    if(request.args.get('show','')):
        limit = int(request.args.get('show',''))
    else:
        limit = PER_PAGE

    if(request.args.get('q','')):
        researchQuery = request.args.get('q','')
    else:
        researchQuery = ''

    if(request.args.get('type','')):
        typeCandidat = request.args.get('type','')
    else:
        typeCandidat = 'all'

    if(request.args.get('sort','')):
        sortData = str(request.args.get('sort',''))
        dirData = str(request.args.get('dir',''))
    else:
        sortData = 'nomCandidat'
        dirData = 'ASC'

    allCandidat = Candidats().getAllCandidat(limit,typeCandidat, sortData, dirData, currentPage, researchQuery)
    
    nbrElements = Candidats().getCountCandidat(typeCandidat,researchQuery)
    
    nbrPage = ceil(nbrElements/limit)
    
    if(nbrElements > 1):
        nbr_elements_courant = (limit * (currentPage-1)) + int(len(allCandidat))
    else:
        nbr_elements_courant = int(len(allCandidat))
    
    searchFields = Candidats().getAllCandidatforSearch()
    search = []
    for item in searchFields:
        data = {"id":item[0],"value":item[1] + " "+item[2]}
        search.append(data)

    jsonSearch = search

    allType = Candidats().getAllType()

    allParti = Partis().getAllPartiforSearch()

    return render_template('candidat.html', activate='candidats', allParti = allParti, allType = allType, jsonSearch = jsonSearch, allCandidat = allCandidat, nbrElements = nbrElements, nbrPage = nbrPage, currentPage = currentPage, nbr_elements_courant = nbr_elements_courant)

@app.route('/addCandidat',methods=['POST'])
def addCandidat():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            nomCandidat = request.form['nomCandidat']
            prenomCandidat = request.form['prenomCandidat']
            date_naissCandidat = request.form['date_naissCandidat']
            lieuNaissCandidat = request.form['lieuNaissCandidat']
            genreCandidat = request.form['genreCandidat']
            TYPECANDIDAT_idType = request.form['TYPECANDIDAT_idType']
            PARTI_numParti = request.form['PARTI_numParti']
            Candidats().add(nomCandidat,prenomCandidat,date_naissCandidat,lieuNaissCandidat,genreCandidat,TYPECANDIDAT_idType,PARTI_numParti)
    flash('Candidat ajouté','success')
    return redirect(url_for('candidats'))

@app.route('/editCandidat',methods=['POST'])
def editCandidat():
    if request.method == 'POST':
        button = request.form['edit']
        if button == 'Enregistrer':
            numCandidat = request.form['numCandidat']
            nomCandidat = request.form['nomCandidat']
            prenomCandidat = request.form['prenomCandidat']
            date_naissCandidat = request.form['date_naissCandidat']
            lieuNaissCandidat = request.form['lieuNaissCandidat']
            genreCandidat = request.form['genreCandidat']
            TYPECANDIDAT_idType = request.form['TYPECANDIDAT_idType']
            PARTI_numParti = request.form['PARTI_numParti']
            Candidats().edit(nomCandidat,prenomCandidat,date_naissCandidat,lieuNaissCandidat,genreCandidat,TYPECANDIDAT_idType,PARTI_numParti,numCandidat)
    flash('Candidat Modifié','success')
    return redirect(url_for('candidats'))

@app.route('/deleteCandidat/<int:numCandidat>')
def deleteCandidat(numCandidat):
    Candidats().delete([numCandidat])
    flash('Candidat supprimée','success')
    return redirect(url_for('candidats'))

# Gestion des electeurs
@app.route('/electeurs/')
def electeurs():

    if(request.args.get('p','')):
        currentPage = int(request.args.get('p',''))
    else:
        currentPage = 1

    if(request.args.get('show','')):
        limit = int(request.args.get('show',''))
    else:
        limit = PER_PAGE

    if(request.args.get('q','')):
        researchQuery = request.args.get('q','')
    else:
        researchQuery = ''

    if(request.args.get('sort','')):
        sortData = str(request.args.get('sort',''))
        dirData = str(request.args.get('dir',''))
    else:
        sortData = 'nomElecteur'
        dirData = 'ASC'

    allElecteur = Electeur().getAllElecteur(limit, sortData, dirData, currentPage, researchQuery)
    
    nbrElements = Electeur().getCountElecteur(researchQuery)
    
    nbrPage = ceil(nbrElements/limit)
    
    if(nbrElements > 1):
        nbr_elements_courant = (limit * (currentPage-1)) + int(len(allElecteur))
    else:
        nbr_elements_courant = int(len(allElecteur))
    
    searchFields = Electeur().getAllElecteurforSearch()
    search = []
    for item in searchFields:
        data = {"id":item[0],"value":item[1] + " "+ item[2]}
        search.append(data)

    jsonSearch = search

    allBureau = Bureau().getAllBureauforSearch()

    return render_template('electeur.html', activate='electeurs', allElecteur = allElecteur, allBureau = allBureau, jsonSearch = jsonSearch, nbrElements = nbrElements, nbrPage = nbrPage, currentPage = currentPage, nbr_elements_courant = nbr_elements_courant)

@app.route('/addElecteur',methods=['POST'])
def addElecteur():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            nomElecteur = request.form['nomElecteur']
            prenomElecteur = request.form['prenomElecteur']
            dateNaissElecteur = request.form['dateNaissElecteur']
            genreElecteur = request.form['genreElecteur']
            numPiece = request.form['numPiece']
            numBureau = request.form['numBureau']
            Electeur().add(nomElecteur,prenomElecteur,dateNaissElecteur,genreElecteur,numPiece,numBureau)
    flash('Electeur ajouté','success')
    return redirect(url_for('electeurs'))

@app.route('/editElecteur',methods=['POST'])
def editElecteur():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            numElecteur = request.form['numElecteur']
            nomElecteur = request.form['nomElecteur']
            prenomElecteur = request.form['prenomElecteur']
            dateNaissElecteur = request.form['dateNaissElecteur']
            genreElecteur = request.form['genreElecteur']
            numPiece = request.form['numPiece']
            numBureau = request.form['numBureau']
            Electeur().edit(numElecteur,nomElecteur,prenomElecteur,dateNaissElecteur,genreElecteur,numPiece,numBureau)
    flash('Electeur Modifié','success')
    return redirect(url_for('electeurs'))

@app.route('/deleteElecteur/<int:numElecteur>')
def deleteElecteur(numElecteur):
    Electeur().delete([numElecteur])
    flash('Electeur supprimée','success')
    return redirect(url_for('electeurs'))


# Gestion des votings
@app.route('/votings/')
def votings():

    if(request.args.get('p','')):
        currentPage = int(request.args.get('p',''))
    else:
        currentPage = 1

    if(request.args.get('show','')):
        limit = int(request.args.get('show',''))
    else:
        limit = PER_PAGE

    if(request.args.get('q','')):
        researchQuery = request.args.get('q','')
    else:
        researchQuery = ''

    if(request.args.get('sort','')):
        sortData = str(request.args.get('sort',''))
        dirData = str(request.args.get('dir',''))
    else:
        sortData = 'nomCandidat'
        dirData = 'ASC'

    if(request.args.get('type','')):
        typeVote = request.args.get('type','')
    else:
        typeVote = 'all'

    if(request.args.get('proc','')):
        proc = request.args.get('proc','')
    else:
        proc = 'all'

    if(request.args.get('voix','')):
        voix = request.args.get('voix','')
    else:
        voix = 'all'

    allVote = Voter().getAllVote(limit,voix,proc,typeVote, sortData, dirData, currentPage, researchQuery)
    
    nbrElements = Voter().getCountVote(voix,proc,typeVote,researchQuery)
    
    nbrPage = ceil(nbrElements/limit)
    
    if(nbrElements > 1):
        nbr_elements_courant = (limit * (currentPage-1)) + int(len(allVote))
    else:
        nbr_elements_courant = int(len(allVote))
    
    searchFields = Voter().getAllVoteforSearch()
    search = []
    for item in searchFields:
        data = {"id":item[0],"value":item[1] + ' ' + item[2]}
        search.append(data)

    jsonSearch = search

    allCandidat = Candidats().getAllCandidatforSearch()
    allElecteur = Electeur().getAllElecteurforSearch()
    allBureau = Bureau().getAllBureauforSearch()
    allType = Candidats().getAllType()
    return render_template('voting.html', activate='votings', jsonSearch = jsonSearch, allType = allType, allCandidat = allCandidat, allElecteur = allElecteur, allBureau = allBureau, allVote = allVote, nbrElements = nbrElements, nbrPage = nbrPage, currentPage = currentPage, nbr_elements_courant = nbr_elements_courant)

@app.route('/addVote', methods=['POST'])
def addVote():
    if request.method == 'POST':
        button = request.form['add']
        if button == 'Enregistrer':
            numCandidat = request.form['numCandidat']
            numElecteur = request.form['numElecteur']
            BUREAU_numBureau = request.form['BUREAU_numBureau']
            Voix = request.form['Voix']
            Procuration = request.form['Procuration']
            typeVote = request.form['typeVote']
            result = Voter().add(numCandidat,numElecteur,BUREAU_numBureau,Voix,Procuration,typeVote)
    if result == True:
        flash('Vote ajouté','success')
    else:
        flash('Vote de l\'electeur dèja repertorié','error')

    return redirect(url_for('votings'))

# Main Principale
if __name__ == '__main__':
    app.run(port=8080,debug=True)
    