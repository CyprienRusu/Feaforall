import os,sys,subprocess

bc = str(GROUPMA).replace("(","{").replace(")","}")

commString="""DEBUT(LANG='EN')

mesh = LIRE_MAILLAGE(UNITE=20)



model = AFFE_MODELE(AFFE=_F(MODELISATION=('3D', ),

                            PHENOMENE='MECANIQUE',

                            TOUT='OUI'),

                    MAILLAGE=mesh)



mater = DEFI_MATERIAU(ELAS=_F(E="""+str(E)+""",

                              NU="""+str(NU)+"""))



fieldmat = AFFE_MATERIAU(AFFE=_F(MATER=(mater, ),

                                 TOUT='OUI'),

                         MODELE=model)



load = AFFE_CHAR_MECA(DDL_IMPO=_F(DX=0.0,

                                  DY=0.0,

                                  DZ=0.0,

                                  GROUP_MA="""+bc+"""),

                      MODELE=model,

                      PRES_REP=_F(GROUP_MA=('"""+str(GROUP)+"""', ),

                                  PRES="""+str(PRES)+"""))



reslin = MECA_STATIQUE(CHAM_MATER=fieldmat,

                       EXCIT=_F(CHARGE=load),

                       MODELE=model)



reslin = CALC_CHAMP(reuse=reslin,

                    CONTRAINTE=('SIGM_ELGA', 'SIGM_ELNO', 'SIGM_NOEU'),

                    RESULTAT=reslin)



IMPR_RESU(RESU=_F(RESULTAT=reslin),

          UNITE=80)

IMPR_RESU(FORMAT='RESULTAT',
          RESU=_F(NOM_CHAM=('DEPL', ),
                  NOM_PARA=('DZ', ),
                  RESULTAT=reslin,
                  VALE_MAX='OUI',
                  VALE_MIN='OUI'),
          UNITE=8)

FIN()"""

commFilePath = os.path.join(savepath, "Stage_1.comm")
commFile = open(commFilePath,'w')
commFile.write(commString)
commFile.close()
