# Short naming system of nanocomposites to find # <!--- TODO : find a name and turn my todo comments in issues haha --->

<!--- Cite main paper here instead of somewhere through the manips? --->

## For ~10 cm plastic preforms, diameter of (CW sizes :I should be able to get from picture if I can't find in text, AP: 12.7 mm for 1/2" ID of PMMA tubes.) ##

<!--- TODO :
_This protocol has been tested so far with styrene._
 Add Cie provider names + grades,  hm moins bon dans un concept de protocole générique. P-e faire un tableau listing of matchig chemicals referred with a, b, c,... in the following list? mwouais non, faire juste styrene direct pour la polymérisation, garder générique juste dans les préliminaires. --->

### Specific Safety Measure ###
When modifiying the core of the protocol, never leave the polymerization completely unattended until the substance is significantly viscous in case of <a href="https://sciencing.com/runaway-polymerization-7556.html">runaway polymerization</a> requiring to immediately turn off heating.

<!--- UNDER CONSTRUCTION, work with Stéphane & David là-dessus, a link to a COPL.ULaval sharepoint intranet would be most appropriate!
All general safety guidelines(?check proper word) from <a href="...">SIMDUT<a/>, <a href="...">SSP</a>, <a href="...">COPL</a> and <a href="link the appropriate wikiOMC section">labOMC</a> continue to apply of course.
TODO : check and implement ULaval's rules for unattended experiments
--->

### Chemicals & Furnitures ###
- 10 mL of purified monomer (AP: 8 mL) 
- Precipitated nanosemiconductors (NSCs) in the desired amount<sup>*</sup>
- 60 mg of benzoyl peroxide as polymerization initiator (Luperox A98) (AP: 120 mg per 15 mL styrene, OMT: initiator-free variant)
- Oven
- Ultrasonic bath with heating
- Venturi pump : filtering flask connected to a vacuum ejector on the water tap
- Light inert gas flow
- Syringe needles
- Glass test tube (?size) with a fitting septum
- Mineral (?check) oil bath with heat-resistant means to hold the tube
- Micropipettes and suitable tips
- Solvents

_N.B. The residual liquid with the NSC precipitate is volatile and in the end may cause some bubbles in the plastic. If this becomes a problem, the liquid can be left to evaporate as long as the cQDs are not dryed out and thus overly exposed to oxygen. A NSC powder could be obtained by evaporation under inert atmosphere, but at this point, we haven't tested how detrimental this is to the photoluminescence (PL)._ 

<sup>*</sup> <!--- TODO : reference the figure in our paper for optical density (?check OD def) guidelines... or include and annotate the figure directly here. --->

### Dispersion of Nanosemiconductors in the Monomer ### 
- Add a known volume of monomers to the tube of precipitated NSCs.
- Hold the tube in an ultrasonic bath briefly to improve NSC dispersion.
- Pour the mixture into a (?size) glass test tube.
- Repeat the previous 3 steps until the NSCs are rinsed out of the centrifuge tube.
- Complete the purified monomer volume in the test tube to 10 mL.
- Add 60 mg of initiator Luperox A98 to the tube.
- Close the with a septum so it can be pierced by syringe needles.

### Degassing & Purging ###
- Put the glass tube under light vacuum with the Venturi pump for a few minutes, with the needle above the liquid level.
- Turn on the heat on the ultrasonic bath and place the tube inside to enhance degassing. <!--- TODO : Rephrase to combine with the last step I think, as it's probably best to do while pumping "kept under vacuum in an ultrasonic bath" --->
- Bubble inert gas through the mixture for a few minutes, with the metal needle below the mixture level. 
- Repeat at least twice to minimize oxygen in the mixture.
- Clean the bubbling needle with hexane, and the vacuum one as well if it touched the mixture.

_N.B. This section aims to protect air-sensitive NSCs by displacing oxygen. It can be shortened for preliminary tests when the PL stability of the nanocomposite at the end is not an issue._
 
### Polymerization Reaction ###
- Keep the test tube in the hot ultrasonic bath (∼60 °C) for ~7 h until the mixture has a syrup-like consistency. <!--- TODO : get a temperature data logger for the ultrasonic bath so we can state an average temperature. --->
- Degas one last time for at least 10 min with the tube still in the hot bath using the Venturi pump. <!--- TODO : Test how long it's actually worth degassing, with a pressure jauge and/or ideaaly with something like a sensor of oxygen and/or air directly in the mixture, as it will likely tends asymptotically towards a pressure equilibrium and thus not worth pumping forever. --->
- Secure the tube in a mineral (check?) oil bath with wire or a metal holder.
- Heat this in the oven at 90°C for ~48 h until fully polymerized. (AP: 90°C for ~48 h, OMT: 140°C for days)
- To avoid a thermal shock, progressively cool the oven back down to room temperature before pulling out the nanocomposite and glassware.

_N.B. The first step with polymerization starting in the bath is required only for experiments on single NSCs, isolated without aggregates in the nanocomposite. Do not skip the following step however, degassing helps to prevent bubbles in the plastic and overpressure from a potential runaway polymerization._


<!--- TO DISCUSS WITH AP, OMT, etc. & ADAPT PROTOCOL AS NEEDED : 
pkoi y'avait du liquide qui sortait du four avec Arthur, cheminée-exhaust avec aiguille touchait la mixture? pkoi la polymérisation d'Olivier-Michel s'emballait et débordait du tube? P-e la dernière étape en surpression d'azote vs sous vide et/ou il n'y avait pas de cheminée? Est-ce que le stockage des préformes est mieux dans le four sous vide ou sous azote? L'azote est probablement mieux pour ralentir la diffusion d'oxygène, mais p-e plus à risque de laisser des bulles lors du processing des préformes? Ehsan & Frej font du moulage sous vide...
--->


<!--- UNDER CONSTRUCTION :
### Nanocomposite Stripping & Annealing ### 
ARTHUR :  Un recuit durant au moins 24 h à 70˚C est ensuite nécessaire afin de libérer les tensions résiduelles du polymère, de même que pour évacuer l’humidité dans le nanocomposite, susceptible de créer des bullesaux interfaces lors de l’étirage.
- Check with Ehsan for a better word than stripping
- consulter pour réduire les chances de se couper sur des tessons de verre
- four sous vide pour bulles, mais pas trop préparer d'avance pour préserver les cQDs
- Storing preforms: azote mais bulles vs done ones in drawer

### Main Observations ###
List pros and cons of the nanocomposite properties that were characterized, referring & linking to the corresponding research notebook entry.

**References**
- our paper, unless it's at the top, but check it for other refs that should be here
- Francesco Meinardi, Annalisa Colombo, Kirill A. Velizhanin, Roberto Simonutti, MonicaLorenzon, Luca Beverina, Ranjani Viswanatha, Victor I. Klimov, and Sergio Brovelli. _Large-area luminescent solar concentrators based on Stokes-shift-engineered nanocrys-tals in a mass-polymerized PMMA matrix._ Nature Photonics 8(5), p. 392–399 (2014). <a href="https://doi.org/10.1038/nphoton.2014.54">https://doi.org/10.1038/nphoton.2014.54</a>

**Resources on nanocomposites** 
- <a href="https://www.mdpi.com/2073-4360/4/1/275">https://www.mdpi.com/2073-4360/4/1/275</a>
--->

<!--- Remove the following versions once the above one is road tested
### Purification du styrène ###
- Pour  préparer les colonnes de purification, compacter une ouate de quartz dans une pipette pasteur. _NOTE : Chaque colonne peut purifier 10-12 ml de styrène._
- Ajouter l'alumine 58 angstoms à l'aide d'un entonnoir.
- Purifier le styrène et mettre de côté.
- Nettoyer les colonnes à l'hexane puis à l'acétone.
- Jeter l'hexane et l'acétone.
- Laisser sécher sous la hotte. Lorsque sèche, vider l'alumine dans la poubelle blanche pour silice (habituellement à côté de la hotte #3) et mettre la pipette pasteur avec la ouate dans la poubelle de verre.
### Purification des cQDs ###
- Verser 32 µl. de cQDs (fiole CW#2 2018/12/19) dans un contenant pour centrifugation
- Remplir à l'éthanol anhydre (habituellement du côté Boudreau)
- Mettre 5 min à 10 000 RPM dans la centrifugeuse. NOTE : Ne pas oublier d'ajouter le Blank si nombre impair de contenant.
- Vider l'éthanol anhydre.
### Préparation des éprouvettes ###
- Ajouter a 0.5 ml de styrène au contenant de centrifugation et disperser les QDs avec le bain ultrasonique. Verser dans l'éprouvette et répéter (1mI total)
- Ajouter le styrène à l'aide d'un septum étanche.
- Seller l'éprouvette à l'aide d'un septum étanche
- Ajouter une aiguille dans le septum (cheminée/exhaust).
- Bubbler à l'azote 3-5 min
- Nettoyer les aiguilles à l'hexane puis à l'acétone. Jeter l'aiguille à usage unique (dans son étuis) dans la poubelle à coté de celle du verre
- Faire le vide par effet Venturi. _NOTE : Attention de ne pas absorber de solution._
- Agiter les éprouvettes  dans le bain sonique 1-2 min pour en retirer les gazes.
- Répéter les étapes 17 et 18 trois fois.
- Enfourner la solution et cuire à 140 °C (4.5 sur le vieux four).
- A chaque 30 min, sortir les éprouvettes et les agiter au bain sonique pendant 1-2 min
- Répéter l'étape 21 jusqu'à ce que le contenu des préformes soit visqueux
### CARLY ###
xTo prepare 10 cm preforms, commercial styrene was first filtered through a column containing Al2O3 particles to remove the polymerization inhibitor. 
x A fixed volume of the cQD solution (Table 1) was further purified by precipitation and centrifugation with isopropyl alcohol then redispersed progressively in styrene and transferred to a glass test tube.
x To initiate the radical polymerization, 60 mg of initiator Luperox A98 per 10 mL of purified styrene was added to the test tube. 
x Oxygen was purged from the sample with nitrogen, and then the tube was sealed and kept under vacuum in an ultrasonic bath for a few minutes to remove residual oxygen.
x  To prevent aggregation of the cQDs, a preliminary polymerization stage was carried out by placing the samples in a heated ultrasonic bath (∼60 °C) for 7 h until the nanocomposite mixture had a syrup-like consistency. 
 x After further removal of residual oxygen within the glass tubes still in the bath, 
x the samples were placed in an oven at 90 °C for 48 h until fully polymerized.
--->



<!---
TODO : The following needs to be moved in its own file for the 2 main heading H1 or otherwise separated and better organized:
--->
# preliminary-methods # 

<!--- UNDER CONSTRUCTION
## Nanosemiconductor Purification ##
- Centrifuge tubes (Eppendorf)
- Micropipettes
TODO : Everything here, the concept and a full detailed protocol needs to be written. The following from Carly can inspire, but it's meant first for synthesis and polymerization: 

CARLY
cQD Synthesis and Dispersion. The cQDs prepared for this study consist of a CdSe core (diameter ∼3.2 nm) surrounded by a CdS shell, which were synthesized following the methods by Nasilowski et al.63 Afterward, the cQDs were purified using several centrifugation cycles with isopropyl alcohol and hexanes as the cQD nonsolvent and solvent, respectively, then redispersed in 10 mL of hexane to obtain a 6 μM concentration.

For polymerization : A fixed volume of the cQD solution (Table 1) was further purified by precipitation and centrifugation with isopropyl alcohol then redispersed progressively in styrene and transferred to a glass test tube.

ARTHUR
En parallèle, un certain volume de cQDs dans une solution d’hexane est transvidé dans un tube de centrifugation. Ce dernier est rempli avec de l’éthanol anhydre, un mauvais solvant permettant de faire agréger les cQDs. Après centrifugation à 10 000rpm pendant 5 minutes,les cQD sont précipités au fond du tube de centrifugation. En remplissant le tube de centrifu-gation de styrène purifié, les cQD peuvent alors être récupérés et transvidés dans l’éprouvette contenant le reste du styrène. Cette purification des cQD permet à la fois de limiter la quan-tité de ligands en sursaturation dans la solution, mais surtout d’éviter d’avoir de l’hexane ensolution lors de la polymérisation. En effet, il a été observé que la présence d’hexane est àl’origine de bulle lors de l’étirage subséquent.


**Resources on Precipitation and Centrifugation**
--->

## Monomer Purification - Milliscale Column Chromatography ##

Monomers are usually stabilized (stab.) with inhibitors preventing unintentional polymerization and should be kept refrigerated (unless it says otherwise on the bottle). A purification step is thus required to get rid of the inhibitors and enable polymerization.
 
## For ~10 cm plastic preforms, diameter of? ##
_This protocol has been tested so far with styrene._

<!--- Add Cie provider names + grades,  hm moins bon dans un concept de protocole générique. P-e faire un tableau listing of matchig chemicals referred with a, b, c,... in the following list? --->
### Chemicals & Furnitures ###
- More than 10 mL of liquid monomer
- Pasteur pipette and its bulb
- Small amount of glass wool and a stick to push it in the pipette
- Funnel fitting the Pasteur pipette 
- Basic alumina powder : Al<sub>2</sub>O<sub>3</sub> particles sieved by a 60 mesh (Alfa Aesar, Brockmann & Schodder activity grade I) 
- Small beakers

### Column Packing ###
- Plug the bottom of the Pasteur pipette with glass wool to prevent the particles from leaking out at the next step. (?with the end chopped off, probably not necessary when pushing with a Pipette bulb)
- Clamp the pipette to a stand.
- Using a funnel, fill the pipette up to its indent with the Al<sub>2</sub>O<sub>3</sub> particles.
- To tamp down the particles by applying air pressure, put the bulb on top of the column and squeeze it, then remove it while still squeezed.

### Monomer Loading ### 
 - Place an empty beaker under the Pasteur pipette to collect the purified monomer.
 - Put more than 10 mL of monomer in another beaker.
 - Pour monomer into the column, nearly filling it.
 - To accelerate the flow, but making sure sure the monomer level does not go below the top of the particles, place the bulb on the pipette and squeeze it, then remove it while still squeezed.
 - Alternatively, let gravity do the work while you do something alse, but keeping an eye on the particles to avoid drying them out.
 - Add monomer to the column until it is all purified.

_N.B. Each column can purify up to ~12 mL of styrene._  
 
## Column Disposal ## 
- Place a container below the Pasteur pipette to transfer waste afterwards in the proper disposal bin.
- Load the column with hexane then acetone to flush out the remaining monomer, again squeezing a bulb on top to accelerate the solvant flow. 
- Empty the waste container into the white plastic jug for nonhalogenated solvents.
- With the container back under the pipette, turn the latter upside down in the clamp.
- Let this dry overnight in a fumehood until the column is emptied of particles, gently tapping it at the end if necessary.
- To speed up drying, air or nitrogen gas(too costly? check with Stéphane) can be flowed through the column.
- Dispose of the particles in the white trash can dedicated to silica and alumina.
- The Pasteur pipette can be reused for the same monomer or put in the glassware waste bin after removing the glass wool.
 
<!--- **Try the slurry method for bigger volumes with the 3it crew** ---> 

**Resources on Column Chromatography**
<!---
TODO : format properly as references, checking my google docs CCV & revtex to settle on a style
--->
- <a href="https://www.orgchemboulder.com/Technique/Procedures/Columnchrom/Procedure.shtml">https://www.orgchemboulder.com/Technique/Procedures/Columnchrom/Procedure.shtml</a> [English]
- <a href="https://www.orgchemboulder.com/Labs/Experiments/8%20-%20Column%20Chromatography.pdf">https://www.orgchemboulder.com/Labs/Experiments/8%20-%20Column%20Chromatography.pdf</a> [English]
- <a href="https://www.orgchemboulder.com/Technique/Procedures/Columnchrom/Columnchrom.shtml">https://www.orgchemboulder.com/Technique/Procedures/Columnchrom/Columnchrom.shtml</a> [English]
- <a href="https://doi.org/10.1002/chemv.201200074">https://doi.org/10.1002/chemv.201200074</a> [English]
- <a href="https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_Lab_Techniques_(Nichols)/02%3A_Chromatography/2.04%3A_Column_Chromatography/2.4B%3A_Microscale_(Pipette)_Columns">https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_Lab_Techniques_(Nichols)/02%3A_Chromatography/2.04%3A_Column_Chromatography/2.4B%3A_Microscale_(Pipette)_Columns</a> [English]
- <a href="https://www.chemistryviews.org/details/education/2040151/Tips_and_Tricks_for_the_Lab_Column_Packing/">https://www.chemistryviews.org/details/education/2040151/Tips_and_Tricks_for_the_Lab_Column_Packing/</a> [English]
- section 2.2 Chromatographie préparative de <a href="https://doi.org/10.51257/a-v2-p1445">https://doi.org/10.51257/a-v2-p1445</a> [French]
- <a href="https://www.silicycle.com/ca/media/pdf/applications/appn-sf002-0-brockmann-schodder-activity-test.pdf">https://www.silicycle.com/ca/media/pdf/applications/appn-sf002-0-brockmann-schodder-activity-test.pdf</a> [English]
<!--- TODO : find a good video from the channels on Quick Notes--->


## Resources on Other Separation Techniques ##
<!---
TODO : format properly as references & add the wikipedia purification page
--->
- <a href="https://fac.umc.edu.dz/inataa/assets/files/Cours-en-Ligne/L2SA/Chimie_analytique_techniques_de_separation.pdf"> https://fac.umc.edu.dz/inataa/assets/files/Cours-en-Ligne/L2SA/Chimie_analytique_techniques_de_separation.pdf</a> [French] <!--- TODO : find a better one --->
- Distillation : <a href="https://www.techniques-ingenieur.fr/base-documentaire/procedes-chimie-bio-agro-th2/operations-unitaires-separation-gaz-liquide-42324210/distillation-absorption-j2610/">https://www.techniques-ingenieur.fr/base-documentaire/procedes-chimie-bio-agro-th2/operations-unitaires-separation-gaz-liquide-42324210/distillation-absorption-j2610/</a> [French]




# basic-techniques # (maybe split between basic and intermediate?)

Proper safety and disposal methods must be learned first, study attentively the wikiOMC page <!--- TODO : ...name & link.. + develop a page on cristal growth like the series starting from http://dx.doi.org/10.1002/chemv.201200103 with lamer models as well and more theory :) + a page on polarity vs polarisability 
--->

## Using a Balance ##
<!---
TODO : add a short text including what is acceptably skipped from the video in our lab
--->
<a href="https://youtu.be/cG6QrqS4ruQ?si=rKG0k026AFvik7i0">https://youtu.be/cG6QrqS4ruQ?si=rKG0k026AFvik7i0</a>

## Using a Vortex Mixer ##
...

## Using an Ultrasonic Bath ##
...

## Using an Oil Bath ##
...Safety.
<a href="https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_Lab_Techniques_(Nichols)/01%3A_General_Techniques/1.04%3A_Heating_and_Cooling_Methods/1.4H%3A_Water_Sand_and_Oil_Baths">https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_Lab_Techniques_(Nichols)/01%3A_General_Techniques/1.04%3A_Heating_and_Cooling_Methods/1.4H%3A_Water_Sand_and_Oil_Baths</a>

## Using a Centrifuge ##
...safety.

- <a href="https://handling-solutions.eppendorf.com/sample-handling/centrifugation/safe-use-of-centrifuges/centrifuge-safety/">https://handling-solutions.eppendorf.com/sample-handling/centrifugation/safe-use-of-centrifuges/centrifuge-safety/</a>
- <a href="https://handling-solutions.eppendorf.com/sample-handling/centrifugation/safe-use-of-centrifuges/basics-in-centrifugation/">https://handling-solutions.eppendorf.com/sample-handling/centrifugation/safe-use-of-centrifuges/basics-in-centrifugation/</a>
- <a href="https://handling-solutions.eppendorf.com/sample-handling/centrifugation/this-and-that/detailview/news/transferring-centrifugation-parameters-from-a-protocol-to-your-own-conditions/">https://handling-solutions.eppendorf.com/sample-handling/centrifugation/this-and-that/detailview/news/transferring-centrifugation-parameters-from-a-protocol-to-your-own-conditions/</a>

## Venturi Effect ##
...
<a href="https://web.uvic.ca/~berryde/techniques/degas.pdf">https://web.uvic.ca/~berryde/techniques/degas.pdf</a>
<!--- TODO : Since pumping and cryogenic techniques seem hard to find (unless I don't have the right keywords?), possibly make a whole wiki section for general degassing and vacuuming, from liguids to vacuum chambers --->

## Using a Schlenk Line ##
... safety. 
<a href="https://schlenklinesurvivalguide.com/">https://schlenklinesurvivalguide.com/</a>

**General Resources**
- <a href="https://chem.libretexts.org/Ancillary_Materials/Demos_Techniques_and_Experiments/General_Lab_Techniques">https://chem.libretexts.org/Ancillary_Materials/Demos_Techniques_and_Experiments/General_Lab_Techniques</a>
- <a href="https://www.chemistryviews.org/?s=tips+and+tricks&orderby=relevance">https://www.chemistryviews.org/?s=tips+and+tricks&orderby=relevance</a>
- <a href="https://edu.rsc.org/interactive-lab-primer-lab-techniques/115379.subject">https://edu.rsc.org/interactive-lab-primer-lab-techniques/115379.subject</a>



