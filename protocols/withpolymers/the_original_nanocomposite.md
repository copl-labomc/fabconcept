# Short naming system of nanocomposites to brainstorm with the team in the new year! Something like comp3D-PS, nano3D-PS, poly3D-PS, PolyOrigin, NanoOrigin, CompOrigin, etc. # <!--- TODO : find a name and turn my todo comments in issues haha --->

<!--- Published in:... Cite main paper here instead of somewhere through the manips? --->

_**For ~10 cm long polystyrene preforms x 13 mm diameter**_ (AP: 12.7 mm for 1/2" ID of PMMA tubes.)

### Specific Safety Measures ###
- When modifiying the core of the protocol, never leave the polymerization completely unattended until the substance is significantly viscous in case of <a href="https://sciencing.com/runaway-polymerization-7556.html">runaway polymerization</a> requiring to immediately turn off heating.
- Check for slow bubbles in the bubbler when opening the inert gas valve. Excessive pressure could build up in the manifold in their absence.
- Do not forget to open the valve on the gas evacuation pipe before turning on the oven, then and close it at the end of the manipulations.
- Never open the oven at high temperature to avoid a thermal shock that could break glass.

<!--- UNDER CONSTRUCTION, work with Stéphane & David là-dessus, a link to a COPL.ULaval sharepoint intranet would be most appropriate!
All general safety guidelines(?check proper word) from <a href="...">SIMDUT</a>, <a href="...">SSP</a>, <a href="...">COPL</a> and <a href="link the appropriate wikiOMC section">labOMC</a> continue to apply of course.
TODO : check and implement ULaval's rules for unattended experiments, develop section Lab safety for Jupyter Notebook, including this <a href="http://www.ilpi.com/safety/index.html">http://www.ilpi.com/safety/index.html</a> as a resource
--->

<!--- TODO : Add Cie provider names + grades of chemicals--->
### Chemicals & Furnitures ###
- 10 mL of purified monomers (AP: 8 mL, especially since 10 mL doesn't fit into the size of test tube specified below!) 
- Precipitated nanosemiconductors (NSCs) in the desired amount<sup>*</sup>
- 60 mg of benzoyl peroxide as polymerization initiator (Luperox A98) (AP: 120 mg per 15 mL styrene, OMT: initiator-free variant)
- Fume hood
- Oven
- Ultrasonic bath with heating
- Venturi pump : filtering flask connected to a vacuum ejector on the water tap
- Light inert gas flow, but it can be hard to adjust directly on the nitrogen line in a fume hood, so a valved bubbler can be employed (!? Hm, risks of forgetting it too closed and ensuing overpressure on the manifold can explode it! Check for a version with a safety valve or something)
- Syringe needles
- 13 mm x 100 mm glass test tube with a fitting airtight septum
- Mineral oil bath with heat-resistant means to hold the tube
- Micropipettes and suitable tips
- Solvents

_N.B. The residual liquid with the NSC precipitate is volatile and may cause some bubbles in the plastic in the end. If this becomes a problem, the liquid can be left to evaporate as long as the NSCs are not dryed out completely and thus overly exposed to oxygen. A NSC powder could be obtained by evaporation under inert atmosphere in principle, but at this point, we haven't tested how detrimental this is to the photoluminescence (PL)._ 

<sup>*</sup> <!--- TODO : annotate include here the figure in our paper for optical density (?check OD def) + cQD concentration of increasingly orange samples <img src="/assets/original_nanocomposite.gif" alt="Optical density of nanocomposites with varying nanosemiconductor concentration"> N.B. if I put the assets folder high up, the asset link might need some dots --->

### Dispersion of Nanosemiconductors in the Monomer ### 
- Add a known volume of purified liquid monomer to the tube of precipitated NSCs.
- Hold the tube in an ultrasonic bath briefly to improve NSC dispersion.
- Pour the mixture into the glass test tube.
- Repeat the previous 3 steps until the NSCs are rinsed out of the centrifuge tube.
- Complete the purified monomer volume in the test tube to 10 mL. (!or 8 mL if we adjust the protocol)
- Add 60 mg of initiator Luperox A98 to the tube. (!or adjusted proportional number)
- Close the test tube with an airtight septum that can be pierced by syringe needles.

### Degassing & Purging ###
- Put the glass tube under light vacuum with the Venturi pump, with the needle above the liquid level.
- Turn on the heat on the ultrasonic bath and place the tube in it to enhance degassing for a few minutes. Note that the polymerization will already accelerate while heating.
- Bubble inert gas through the mixture for a few minutes, with the metal needle below the mixture level and adding a second one above the liquid as exhaust. 
- Repeat at least twice to minimize oxygen in the mixture. <!--- TODO : find out if it's better to finish under vacuum or under nitrogen considering light diffusion, potential glass tube breaking and dissolved gases that could lead to bubbles during fiber drawing, then adjust the last step here if needed. --->
- Clean the bubbling needle with hexane, and the vacuum one as well if it touched the mixture.

_N.B. This section aims to protect air-sensitive NSCs by displacing oxygen. It can be shortened for preliminary tests when light diffusion (? to check if it's really correlated to oxygen or just any gas like nitogen, then and put explanation at the beginning of sentence) and PL stability of the resulting nanocomposite are not an issue._

### Polymerization Reaction ###
- Keep the test tube under vacuum in the hot ultrasonic bath (∼60 °C) for ~7 h until the mixture has a syrup-like consistency. <!--- TODO merge with next TODO too(!): watch out for potential glass breaking & get a temperature data logger for the ultrasonic bath so we can state an average temperature. (If glass breaking prevents vacuuming all the time and/or we are concious about wasting water, add this step "- Degas one last time for at least 10 min with the tube still in the hot bath using the Venturi pump." and possibly a nitrogen purge if we find out if it's better to finish on this. TODO : If possible, test how long it's actually worth degassing, with a pressure jauge and/or idealy with something like a sensor of oxygen and/or air directly in the mixture, as it will likely tends asymptotically towards a pressure equilibrium and thus not worth pumping forever. That might also help pinpoint the conditions in which the small test tubes tend to break during polymerization :( --->
- Secure the tube in a mineral oil bath with wire or a heat-resistant holder.
- Open the valve on top of the pipe behind the oven to ensure proper evacuation.
- Place the glass tube assembly in the oven.
- Heat at 90°C for ~48 h until fully polymerized. (AP: 90°C for ~48 h, OMT: 140°C for days)
- Progressively cool the oven back down to room temperature before pulling out the nanocomposite and glassware. Note that the oven's timer can stop heating automatically :smiley:.
- Close the exhaust pipe valve.

_N.B. The first step with polymerization starting in the bath is required only for experiments on single NSCs, isolated without aggregates in the nanocomposite._ <!--- Adapt this according to our findings relative to overpressure vs underpressure in the glass tube : Do not skip the following step however, degassing helps to prevent bubbles in the plastic and overpressure from a potential runaway polymerization.--->

<!--- TO DISCUSS WITH AP, OMT, etc. & ADAPT PROTOCOL AS NEEDED : 
Investigate glass beaking cause: implosion(vacuum underpressure) or explosion (nitrogen over pressure in relation with pkoi y'avait du liquide qui sortait du four avec Arthur, cheminée-exhaust avec aiguille touchait la mixture? pkoi la polymérisation d'Olivier-Michel s'emballait et débordait du tube? P-e la dernière étape en surpression d'azote vs sous vide et/ou il n'y avait pas de cheminée? Est-ce que le stockage des préformes est mieux dans le four sous vide ou sous azote? L'azote est probablement mieux pour ralentir la diffusion d'oxygène, mais p-e plus à risque de laisser des bulles lors du processing des préformes? Ehsan & Frej font du moulage sous vide...
--->

<!--- UNDER CONSTRUCTION :
### Nanocomposite Stripping & Annealing ### 
ARTHUR :  Un recuit durant au moins 24 h à 70˚C est ensuite nécessaire afin de libérer les tensions résiduelles du polymère, de même que pour évacuer l’humidité dans le nanocomposite, susceptible de créer des bullesaux interfaces lors de l’étirage.
- Check with Ehsan for a better word than stripping
- consulter pour réduire les chances de se couper sur des tessons de verre
- four sous vide pour bulles, mais pas trop préparer d'avance pour préserver les NSCs
- Storing preforms: azote mais bulles vs done ones in drawer

### Main Observations ###
- The nanocomposite volume shrinks by ~...% relative to the initial monomer, thus NSC doping concentrations must be re-calculated accordingly. (TODO: evaluate by water dispoacement and check if it tracks with calculations from absorption curves of cQD cores b4 vs after.)
-...
Also list pros and cons of the nanocomposite properties that were characterized, referring & linking to the example sample and research notebook Airtable records.

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
- Fume Hood
- Centrifuge tubes (Eppendorf)
- Micropipettes and suitable tips
- Solvents
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
_This protocol has been tested so far with styrene from ...._

<!--- TODO: Add Cie providing monomer + grades above, hm moins bon dans un concept de protocole générique. P-e tourner en tableau listing of matching chemicals referred with a, b, c,... si ça s'allonge et qu'il faut modifier les particules ou autre pour que ça marche? Also confirm how much monomer a single column can purify and modify the N.B. as needed. --->
### Chemicals & Furnitures ###
- Slightly more than the amount of liquid monomer required for the polymerization
- Pasteur pipette and its bulb
- Small amount of glass wool and a stick to push it in the pipette
- Funnel fitting the Pasteur pipette 
- Basic alumina powder : Al<sub>2</sub>O<sub>3</sub> particles sieved by a 60 mesh (Alfa Aesar, Brockmann & Schodder activity grade I) 
- Micropipettes and suitable tips
- Small beakers

### Column Packing ###
- Plug the bottom of the Pasteur pipette with glass wool to prevent the particles from leaking out at the next step.
- Clamp the pipette to a stand.
- Using a funnel, fill the pipette up to its indent with the Al<sub>2</sub>O<sub>3</sub> particles.
- To tamp down the particles by applying air pressure, put the bulb on top of the column and squeeze it, then remove it while still squeezed.

_N.B. Each column can purify up to ~12 mL of styrene._  

### Monomer Loading ### 
 - Place an empty beaker under the Pasteur pipette to collect the purified monomer.
 - Put the desired amount of monomer in another beaker.
 - With a micropipette, pour some monomer liquid into the column, nearly filling it.
 - To accelerate the flow while making sure sure the monomer level does not go below the top of the particles, place the bulb on the pipette and squeeze it, then remove it while still squeezed.
 - Alternatively, let gravity do the work while you do something alse, but keeping an eye on the particles to avoid drying them out.
 - Add monomer to the column until it is all purified. 
 
## Column Disposal ## 
- Place a container below the Pasteur pipette to transfer waste afterwards in the proper disposal bin.
- Load the column with hexane then acetone to flush out remaining monomers, again squeezing a bulb on top to accelerate the solvent flow. 
- Empty the waste container into the white plastic jug for nonhalogenated solvents.
- With the container back under the pipette, turn the latter upside down in the clamp.
- Let this dry overnight in a fumehood until the column is emptied of particles, gently tapping it at the end if necessary.
- To speed up drying, air or nitrogen gas(too costly? check with Stéphane) can be flowed through the column.
- Dispose of the alumina particles in the white trash can dedicated to them.
- The Pasteur pipette can be reused for the same monomer or put in the glassware waste bin after removing the glass wool.
 
<!--- TODO: Eventually try the slurry method for bigger volumes ---> 

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
- <a href="https://fac.umc.edu.dz/inataa/assets/files/Cours-en-Ligne/L2SA/Chimie_analytique_techniques_de_separation.pdf"> https://fac.umc.edu.dz/inataa/assets/files/Cours-en-Ligne/L2SA/Chimie_analytique_techniques_de_separation.pdf</a> [French] <!--- TODO : find a better one --->
- Distillation : <a href="https://www.techniques-ingenieur.fr/base-documentaire/procedes-chimie-bio-agro-th2/operations-unitaires-separation-gaz-liquide-42324210/distillation-absorption-j2610/">https://www.techniques-ingenieur.fr/base-documentaire/procedes-chimie-bio-agro-th2/operations-unitaires-separation-gaz-liquide-42324210/distillation-absorption-j2610/</a> [French]



<!---
TODO : format properly as references & add the wikipedia purification page
--->
# basic-techniques # (maybe split between basic and intermediate?)

Proper safety and disposal methods must be learned first, study attentively the wikiOMC page <!--- TODO : ...name & link.. + develop a page on cristal growth like the series starting from http://dx.doi.org/10.1002/chemv.201200103 with lamer models as well and more theory :) + a page on polarity vs polarisability 
--->

## Vacuum & cryogenics ##
...safety
TODO: Voir avec Mario pour nous trouver une bonne formation de l'AVS ou autre


## Using a Balance ##
<!---
TODO : add a short text including what is acceptably skipped from the video in our lab
--->
<a href="https://youtu.be/cG6QrqS4ruQ?si=rKG0k026AFvik7i0">https://youtu.be/cG6QrqS4ruQ?si=rKG0k026AFvik7i0</a>

## Using a Vortex Mixer ##
...

## Ultrasonication ##
...

## Using an Oil Bath ##
...Safety.
<a href="https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_Lab_Techniques_(Nichols)/01%3A_General_Techniques/1.04%3A_Heating_and_Cooling_Methods/1.4H%3A_Water_Sand_and_Oil_Baths">https://chem.libretexts.org/Bookshelves/Organic_Chemistry/Organic_Chemistry_Lab_Techniques_(Nichols)/01%3A_General_Techniques/1.04%3A_Heating_and_Cooling_Methods/1.4H%3A_Water_Sand_and_Oil_Baths</a>

## Centrifugation ##
...safety.

- <a href="https://handling-solutions.eppendorf.com/sample-handling/centrifugation/safe-use-of-centrifuges/centrifuge-safety/">https://handling-solutions.eppendorf.com/sample-handling/centrifugation/safe-use-of-centrifuges/centrifuge-safety/</a>
- <a href="https://handling-solutions.eppendorf.com/sample-handling/centrifugation/safe-use-of-centrifuges/basics-in-centrifugation/">https://handling-solutions.eppendorf.com/sample-handling/centrifugation/safe-use-of-centrifuges/basics-in-centrifugation/</a>
- <a href="https://handling-solutions.eppendorf.com/sample-handling/centrifugation/this-and-that/detailview/news/transferring-centrifugation-parameters-from-a-protocol-to-your-own-conditions/">https://handling-solutions.eppendorf.com/sample-handling/centrifugation/this-and-that/detailview/news/transferring-centrifugation-parameters-from-a-protocol-to-your-own-conditions/</a>

## Venturi Effect ##
...
<a href="https://web.uvic.ca/~berryde/techniques/degas.pdf">https://web.uvic.ca/~berryde/techniques/degas.pdf</a>
<!--- TODO : Since pumping and cryogenic techniques seem hard to find (unless I don't have the right keywords?), possibly make a whole wiki section for general degassing and vacuuming, from liguids to vacuum chambers --->

## Cleaning Glassware ##
- NSC synthesis flasks...Bain de bases : KOH + EtOH + 1 ou i-P??OH, I can't read the last one on the pails :(

## Using a Glovebox ##
... safety
<a href="http://www.ilpi.com/inorganic/glassware/glovebox.html">http://www.ilpi.com/inorganic/glassware/glovebox.html</a>


## Using a Schlenk Line ##
... safety. <a href="http://www.ilpi.com/inorganic/glassware/vacline.html">http://www.ilpi.com/inorganic/glassware/vacline.html</a>

Copy pasted from resources, to adapt : To maintain a positive pressure on a reaction that is simply stirring, the bubbler should bubble once every few seconds. A greater flow wastes nitrogen and can bubble away volatile solvents. A lesser flow increases the chances of air diffusing into your apparatus.
To prevent oil or mercury from splashing out of your bubbler, connect a piece of Tygon tubing to the outlet.

- <a href="https://schlenklinesurvivalguide.com/">https://schlenklinesurvivalguide.com/</a>
- <a href="http://www.ilpi.com/inorganic/glassware/index.html">http://www.ilpi.com/inorganic/glassware/index.html</a>

## General Resources ##
- <a href="https://chem.libretexts.org/Ancillary_Materials/Demos_Techniques_and_Experiments/General_Lab_Techniques">https://chem.libretexts.org/Ancillary_Materials/Demos_Techniques_and_Experiments/General_Lab_Techniques</a>
- <a href="https://www.chemistryviews.org/?s=tips+and+tricks&orderby=relevance">https://www.chemistryviews.org/?s=tips+and+tricks&orderby=relevance</a>
- <a href="https://edu.rsc.org/interactive-lab-primer-lab-techniques/115379.subject">https://edu.rsc.org/interactive-lab-primer-lab-techniques/115379.subject</a>



