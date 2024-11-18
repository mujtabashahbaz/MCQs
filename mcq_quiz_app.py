import streamlit as st
import random
import re

# Paste the content of the MCQs document here
mcqs_text = """
QUESTION 1
A 53-year-old woman is seen in the general surgical outpatient clinic. She attended her GP with a 1-month history of upper abdominal pain and was found to have a palpable, firm mass in the epigastrium. An upper gastrointestinal (GI) endoscopy is normal and the surgical team requests a contrast-enhanced CT of the abdomen. This demonstrates a multicystic mass in the pancreas. Which findings would make a mucinous cystic tumour more likely than a serous cystadenoma?
Central stellate calcification is present within the lesion.
The mass contains 12 separate cysts.
The smallest cystic component measures 28 mm in diameter.
The patient has a known diagnosis of von Hippel-Lindau disease.
The tumour is located in the head of the pancreas.
ANSWER: C
Mucinous cystic pancreatic tumours (cystadenomas and cystadenocarcinomas) typically contain a few large cysts, each measuring more than 20 mm in diameter.
Reference: Grainger & Allison’s 5e, pp 804-806.


QUESTION 2
A 54-year-old man with hepatitis B cirrhosis attends the hepatology outpatient clinic. The patient’s serum alpha fetoprotein level is found to be significantly elevated, having been normal 6 months ago. An abdominal ultrasound demonstrates a new 3-cm lesion in the right lobe of the liver, and a diagnosis of hepatocellular carcinoma (HCC) is suspected. Which one of the following statements is correct regarding HCC?
Brain metastases are hypovascular and calcified.
HCC derives its blood supply primarily from the hepatic artery.
Portal vein invasion is more suggestive of a liver metastasis than HCC.
Small HCC (< 1 cm) are typically heterogeneous and hyperechoic on US.
The bony skeleton is the most common site for distant metastases.
ANSWER: B
HCC derives its blood supply from the hepatic artery (hence the rapid arterial phase enhancement). A large HCC will usually demonstrate heterogeneous reflectivity due to areas of necrosis, but smaller lesions are typically of homogeneous low reflectivity on ultrasound. HCC often invades the branches of the portal vein and the most frequent site of metastases is the lungs. Metastases to the brain are typically hypervascular and do not usually contain calcification.
Reference: Yu SCH, Yeung DTK, So NMC. Imaging features of hepatocellular carcinoma Clin Radiol 2004;59:145-156.


QUESTION 3
A 22-year-old man is brought to the Emergency Department with a 2-day history of increasingly severe upper abdominal pain and vomiting. He has not opened his bowels for 24 hours but has passed flatus. The patient is usually fit and well but admits to consuming 100 units of alcohol per week. Initial laboratory investigations show an elevated white cell count and a significantly raised serum amylase. An abdominal radiograph is performed and demonstrates a single segment of dilated small bowel in the central abdomen. What name is given to this radiographic finding?
Arrowhead sign
Bird of prey sign
Football sign
Ranson’s sign
Sentinel loop sign
ANSWER: E
A localised paralytic ileus due to inflammatory change in the pancreas is known as the sentinel loop sign.
Reference: Grainger & Allison’s 5e, pp 598, 793-798.


QUESTION 4
A 72-year-old man presents to his GP with increasing dyspepsia and weight loss. He has not experienced any other GI symptoms, and physical examination is unremarkable. A barium meal is performed with the administration of intravenous Buscopan. The oesophagus is normal in appearance, but a ‘bull’s eye’ lesion is noted in the gastric mucosa. Which one of the following is not a recognised cause of this appearance?
Gastric carcinoma
Gastrointestinal stromal tumour (GIST)
Magenstrasse
Melanoma metastases
Neurofibromatosis
ANSWER: C
Magenstrasse refers to the normal longitudinal mucosal folds seen adjacent to the lesser curve of the stomach during a barium meal. The ‘bull’s eye’ appearance seen during a barium meal is due to a central ulcer in an elevated area of submucosa. A GIST may well have this appearance and neurofibromatosis can cause single or multiple target lesions. Melanoma is the commonest cause of submucosal gastric metastases.
Reference: Chapman S, Nakielny R. Aids to Radiological Differential Diagnosis, 5th edition (Edinburgh: Saunders, 2003), p 136.


QUESTION 5
A 19-year-old female student presents with acute abdominal pain, elevated CRP, and a low-grade temperature. On clinical examination, there is tenderness to light palpation in the right iliac fossa, and the patient is febrile. A graded compression ultrasound examination is performed. Which one of the following statements is true?
A transverse appendiceal diameter of 5 mm is diagnostic of acute appendicitis.
The finding of a pelvic fluid collection makes a diagnosis of acute appendicitis unlikely.
The presence of hyperechoic fat in the right iliac fossa makes a diagnosis of acute appendicitis unlikely.
The sensitivity of graded compression ultrasound in suspected acute appendicitis is 75—90%.
The specificity of graded compression ultrasound in suspected acute appendicitis is 35—50%.
ANSWER: D
Graded compression ultrasound of the appendix can avoid unnecessary surgery and ionising radiation—particularly relevant for children and women of childbearing age. The finding of a noncompressible appendix with a transverse diameter of 6 mm or greater is highly suggestive of acute appendicitis (specificity 86-100%). Other ultrasound findings include hyperechoic fat in the right iliac fossa, periappendiceal fluid or a pelvic fluid collection (appendiceal abscess).
Reference: Gracey D, McClure MJ. The impact of ultrasound in suspected acute appendicitis. Clin Radiol 2007;62:573-578.


QUESTION 6
A 42-year-old man presents to the Emergency Department with a 7-day history of severe bloody diarrhoea and abdominal pain. He has previously been fit and well with no significant medical history. On examination, the patient is dehydrated with generalized abdominal tenderness but no clinical evidence of peritonism. An abdominal radiograph is performed. Which radiographic finding would be most suggestive of a toxic megacolon?
Caecum measuring 4.5 cm in diameter
Multiple mucosal islands in a dilated transverse colon
Pseudodiverticulae in the descending colon
Thickened haustrae throughout the entire colon
‘Thumbprinting’ of the transverse and descending colon
ANSWER: B
The presence of severe ulceration leading to mucosal islands is a major sign of toxic megacolon (the other key finding is colonic dilatation > 5 cm).
Reference: Grainger & Allison’s 5e, p 696.


QUESTION 7
A 54-year-old woman attends a well woman clinic and is found to have abnormal liver function tests. She is referred to the hepatology outpatient clinic, and an abdominal ultrasound is performed. This demonstrates diffuse increased reflectivity of the liver parenchyma but no focal parenchymal abnormality. The hepatology team request an ultrasound-guided percutaneous liver biopsy. Which statement is true regarding this procedure?
Ten to 20% of complications occur in the first 2 hours post-procedure.
Ascites is an absolute contraindication to percutaneous liver biopsy.
Mortality rate is 1 in 500.
Over 90% of complications occur in the first 24 hours post-procedure.
There is no increased risk of complications with malignant liver lesions.
ANSWER: D
Following an ultrasound-guided liver biopsy, nearly two-thirds of complications occur in the first 2 hours, with 96% of complications having occurred by 24 hours.
Reference: Grainger & Allison’s 5e, pp 758-759.


QUESTION 8
A 26-year-old man presents to the Emergency Department with acute epigastric pain and vomiting. The serum amylase is found to be markedly elevated, and the patient is treated for acute pancreatitis. A contrast-enhanced CT of the abdomen is subsequently performed and demonstrates calcification throughout the pancreas. Bilateral renal calculi are also noted. What is the most likely underlying diagnosis?
Hereditary pancreatitis
Hyperparathyroidism
Hypoparathyroidism
Mucinous cystadenocarcinoma
Multiple pancreatic pseudocysts
ANSWER: B
A significant minority of patients with hyperparathyroidism will develop acute pancreatitis and around 30% of these patients develop pancreatic calcification. Hypoparathyroidism is associated with calcification in the soft tissues but pancreatic calcification is not a recognised feature. Hereditary pancreatitis is an autosomal dominant condition with 60% of patients demonstrating round, coarse calcification of the pancreas.
Reference: Chapman & Nakielny, Aids to Radiological Differential Diagnosis, pp 181—182.


QUESTION 9
A 53-year-old man has a history of type 2 diabetes mellitus and nonalcoholic steatohepatitis. He complains of weight loss and malaise; therefore, an abdominal ultrasound is performed. This demonstrates a 2-cm focal lesion in the liver parenchyma. Which additional findings would be most consistent with an area of focal fatty sparing in hepatic steatosis?
There is avid enhancement of the lesion on contrast-enhanced ultrasound.
The focal area is of increased echogenicity compared to that of the surrounding liver.
The lesion has a geographic margin and is of reduced echogenicity compared to that of the surrounding liver.
The lesion is hypoechoic with vessels displaced around its margins.
The lesion is in the gallbladder fossa and is associated with segmental intrahepatic biliary dilatation.
ANSWER: C
Focal fatty sparing usually leads to geographic or wedge-shaped lesions of reduced echogenicity. There should be no mass effect or abnormal enhancement characteristics in focal fatty sparing or infiltration. Both focal fatty sparing and infiltration typically occur in sites such as the gallbladder fossa, falciform ligament and porta hepatis, due to the altered venous drainage of these areas.
Reference: Karcaaltincaba M, Akhan O. Imaging of hepatic steatosis and fatty sparing. Eur J Radiol 2007;61:33-43.


QUESTION 10
A 29-year-old man presents with a 6-month history of dysphagia, associated with retrosternal pain. A barium swallow demonstrates a markedly dilated oesophagus containing food debris. There is a smooth narrowing of the distal oesophagus with barium intermittently spurting into the stomach. What is the most likely diagnosis?
Oesophageal achalasia
Oesophageal leiomyoma
Paraoesophageal hiatus hernia
Peptic oesophageal stricture
Squamous cell carcinoma of the oesophagus
ANSWER: A
Clinical features of oesophageal achalasia also include relief of retrosternal pain with carbonated and hot drinks (relaxes the lower oesophageal sphincter).
Reference: Grainger & Allison’s 5e, p 621.


QUESTION 11
A 68-year-old woman presents with malaise and abdominal pain and is found to have abnormal liver function tests. An abdominal ultrasound identifies multiple hyperechoic lesions in the liver, and contrast-enhanced CT of the abdomen demonstrates that these are hypervascular liver metastases. Given the CT findings, what is the most likely underlying diagnosis?
Carcinoid
Lymphoma
Non-small-cell lung cancer
Ovarian epithelial carcinoma
Transitional cell carcinoma (TCC) of bladder
ANSWER: A
Most liver metastases are hypovascular and appear as lower attenuation than normal liver parenchyma on portal venous phase CT. Hypervascular metastases are less common and appear most prominently during the arterial phase (20-30 s) post-contrast. Common causes of hypervascular liver metastases include carcinoid, melanoma, thyroid, and renal cancer.
Reference: Chapman & Nakielny, Aids to Radiological Differential Diagnosis, pp 172-173.


QUESTION 12
A 35-year-old pregnant woman (28 weeks gestation) presents to her GP with right upper quadrant abdominal pain and is found to have abnormal liver function tests. An abdominal ultrasound is performed and demonstrates a diffusely hyperechoic liver with a discrete 4-cm hypoechoic lesion in the right lobe. An MRI is performed 3 weeks later, showing that the liver lesion has increased in size, now measuring 7 cm in diameter. The lesion is isointense on in-phase T1-weighted images, losing signal on out-of-phase images. Following intravenous gadolinium, there is immediate and intense enhancement with early washout. What is the most likely diagnosis?
Choriocarcinoma
Focal nodular hyperplasia
Hepatic adenoma
Liver haemangioma
Metastatic breast cancer
ANSWER: C
The MRI findings are highly suggestive of a hepatic adenoma, and the history of rapid growth during pregnancy supports this diagnosis.
Reference: Grainger & Allison’s 5e, pp 741–742.



QUESTION 13
A 59-year-old man undergoes surgical resection of a rectal tumour. A contrast-enhanced CT of the abdomen is performed 3 months later and demonstrates a new, solitary 3-cm liver metastasis. The lesion lies inferior to the level of the left and right portal veins and posterior to the right hepatic vein. The remainder of the CT examination is unremarkable and the patient is assessed for surgical resection of the liver lesion. Which segment of the liver does the liver metastasis lie in?
Segment 4b
Segment 5
Segment 6
Segment 7
Segment 8
ANSWER: C
The Couinaud classification divides the liver into 8 independent segments, each with its own vascular supply and biliary drainage. This classification is crucial for resectable liver lesions, such as solitary colorectal metastasis.
Reference: Chapman & Nakielny, Aids to Radiological Differential Diagnosis, p 166.


QUESTION 14
A 74-year-old man presents with an 8-week history of altered bowel habit and rectal bleeding. A flexible sigmoidoscopy demonstrates a malignant stricture in the rectum and biopsies confirm rectal adenocarcinoma. An MRI is performed and shows an annular neoplasm at 12 cm. The mass invades 4 mm beyond the rectal wall into the perirectal fat and infiltrates the peritoneal reflection anteriorly. There is a small volume of free peritoneal fluid. What is the radiological T stage?
TX
T1
T2
T3
T4
ANSWER: E
Evidence of peritoneal invasion indicates stage T4 rectal cancer.
Reference: Grainger & Allison’s 5e, pp 689-690.

QUESTION 15
A 38-year-old woman receives an orthotopic liver transplant for chronic liver failure due to primary biliary cirrhosis. The patient’s liver enzyme levels become markedly elevated after 24 hours and her clinical condition deteriorates. An abdominal ultrasound is performed with Doppler evaluation of the hepatic vessels. Given the clinical history, which vascular complication is most likely to have occurred?
Arterioportal fistula
IVC thrombosis
Hepatic artery stenosis
Hepatic artery thrombosis
Portal vein thrombosis
ANSWER: D
Hepatic artery thrombosis is the most common and serious early vascular complication post liver transplant. Diagnosis is essential, as thrombolysis may be necessary, but retransplantation is often required.
Reference: Federle MP, Kapoor V. Complications of liver transplantation: imaging and intervention. Radiol Clinics North Am 2003; 41(6):1289-1305.


QUESTION 16
A 37-year-old man presents to his GP with increasing right upper quadrant pain. On examination, he is afebrile with right upper quadrant tenderness and fullness. An abdominal ultrasound is performed and demonstrates a 5-cm diameter cystic lesion in the right lobe of liver. The mass contains multiple septations with a large cyst centrally and multiple small cystic spaces peripherally. Echogenic debris is seen within the cystic lesion and alters in position when the patient lies on his side. From the clinical and sonographic details, what is the most likely diagnosis?
Amoebic abscess
Hydatid cyst
Pyogenic liver abscess
Simple liver cyst
Solitary metastasis
ANSWER: B
A multiloculated cystic mass with daughter cysts and echogenic debris (‘hydatid sand’) is characteristic of a hydatid liver cyst.
Reference: Grainger & Allison’s 5e, pp 736-737.


QUESTION 17
A 48-year-old woman is noted to have elevated liver enzymes on blood tests performed by her GP. She attends the radiology department and an abdominal ultrasound is performed. This demonstrates moderate diffuse fatty infiltration of the liver and thickening of the wall of the gallbladder fundus. Hyperechoic foci are seen in the gallbladder wall with ‘ring-down’ reverberation artefacts. There is no acoustic shadowing. What is the most likely diagnosis?
Adenomyomatosis
Chronic cholecystitis
Multiple gallstones with acute cholecystitis
Porcelain gallbladder
Xanthogranulomatous cholecystitis
ANSWER: A
Cholesterol crystals within Rokitansky-Aschoff sinuses produce the characteristic ‘comet tail’ or ring-down artefact seen in adenomyomatosis.
Reference: Gore RM, Yaghmai V, Newmark GM, et al. Imaging benign and malignant disease of the gallbladder. Radiol Clin North Am 2002; 40(6):1307-1323.


QUESTION 18
A 68-year-old man presents to his GP with a 1-month history of epigastric pain, vomiting, and mild weight loss. Examination is unremarkable and the patient is referred for an upper gastrointestinal endoscopy. This demonstrates mild gastritis with biopsies positive for Helicobacter pylori and he is commenced on eradication therapy. Three months later, the symptoms have persisted and the patient has lost 5 kg in weight. A double contrast barium meal is performed and reveals a shallow ulcer on the lesser curve of the stomach. Which additional finding would make the ulcer more likely to be benign than malignant?
Hampton’s line is present.
Nodular mucosal folds stop at the edge of the lesion.
The ulcer does not extend beyond the gastric wall.
The ulcer has an irregular margin.
The ulcer measures 40 mm in size.
ANSWER: A
Hampton’s line refers to a lucent line crossing the ulcer base, highly suggestive of a benign ulcer.
Reference: Grainger & Allison’s 5e, pp 633-634.


QUESTION 19
A 42-year-old man has type 1 diabetes mellitus. Despite intensive medical management, the patient’s glycemic control remains problematic, and he receives a cadaveric pancreatic transplant with the pancreatic graft anastomosed to the right common iliac artery. Four days following surgery, the clinical team is concerned about the pancreatic graft function and requests radiological assessment for post-transplant complications. Which one of the following statements is true regarding pancreatic transplant imaging?
In acute rejection, the pancreatic graft is small and hyperechoic on ultrasound.
Pancreatic exocrine secretions often drain into the urinary bladder.
Radionuclide imaging with Tc-99m-pertechnetate is the most sensitive way of detecting acute pancreatic rejection.
Surgical complications are more common following renal transplantation than pancreatic transplantation.
Transplant pancreatitis is very rare in the first 48 hours post-surgery.
ANSWER: B
Formation of a cystoduodenostomy drains the exocrine pancreatic secretions into a duodenal loop, anastomosed directly with the urinary bladder.
Reference: Grainger & Allison’s 5e, p 807.


QUESTION 20
A 49-year-old man presents to his GP with increasing dysphagia and weight loss. Upper gastrointestinal endoscopy reveals a tumour in the distal oesophagus and biopsies confirm oesophageal adenocarcinoma. The patient undergoes a contrast-enhanced CT of the chest and abdomen which shows mucosal thickening in the distal oesophagus but no other abnormality. An endoscopic ultrasound is performed and shows that the tumour infiltrates through the muscularis propria and adventitia but does not extend beyond the serosa. A round 13-mm peritumoral node is noted. From this information, what is the TNM staging of this tumour?
T2 N0 M0
T2 N1 M0
T3 N0 M0
T3 N1 M0
T4 N1 M0
ANSWER: D
In oesophageal cancer, T1 tumours are limited to the mucosa, T2 tumours invade the muscularis propria, T3 lesions extend into the adventitia, and T4 lesions breach the serosal surface and can invade surrounding structures.
Reference: Grainger & Allison’s 5e, pp 616-619.


QUESTION 21
A male patient is referred to the on-call surgical team with a 3-day history of generalized abdominal pain and vomiting. The patient has not opened his bowels for 2 days. Examination reveals a distended abdomen with increased bowel sounds. An abdominal radiograph is performed and demonstrates a large dilated loop of large bowel with several loops of dilated small bowel centrally. Which other feature would make a diagnosis of caecal volvulus more likely than that of sigmoid volvulus?
Haustrae are visible in the gas-filled viscus.
The apex of the viscus lies in the left upper quadrant.
The patient is 75 years old.
The patient is in long-term institutional care.
The viscus rises above the level of the T10 vertebral body.
ANSWER: A
The presence of haustrations in a dilated viscus and gas in the appendix are key to the diagnosis of caecal volvulus.
Reference: Grainger & Allison’s 5e, pp 597-598.


QUESTION 22
A 59-year-old man is diagnosed with squamous cell carcinoma of the lower oesophagus. A contrast-enhanced CT of the chest and abdomen demonstrates a right paratracheal lymph node that measures 9 mm in the short axis, with no evidence of distant metastases. The patient is considered for surgery and a PET-CT examination is performed. The PET-CT demonstrates no uptake in the right paratracheal lymph node, but there is symmetrical uptake of 18-FDG in both supraclavicular areas. What is the most likely explanation for this finding?
Brown adipose tissue
Paraneoplastic polymyositis
Recent trauma
Recent viral upper respiratory tract infection
Uncontrolled diabetes mellitus
ANSWER: A
Brown fat is a well-recognised physiological cause of 18-FDG uptake. Hyperglycaemia likely reduces 18-FDG uptake as it competes with glucose for uptake into metabolically active cells.
Reference: El-Haddad G, Aiavi A, Mavi A, et al. Normal variants in [18F]-fluorodeoxyglucose PET imaging. Radiol Clin North Am 2003; 42(6): 1063-1081.


QUESTION 23
A 52-year-old female patient is under the care of a rheumatologist with a diagnosis of diffuse scleroderma. She presents to her GP with vomiting, intermittent abdominal pain, and reduced bowel habit. An abdominal radiograph demonstrates several loops of gas-filled bowel, but there is no evidence of mechanical obstruction. A barium follow-through examination is performed. In view of the clinical history, what are the most likely findings?
Dilated small bowel with increased number of valvulae conniventes
Extraluminal mass in the ileum, causing ulceration and a shouldered stricture
Long irregular ileal stricture with antimesenteric mucosal thickening
Nodular thickening of the valvulae conniventes of the duodenum only
Short stricture in the terminal ileum with ‘cobblestoning’ of the mucosa
ANSWER: A
This describes the characteristic ‘hide bound’ appearance of the small bowel in scleroderma.
Reference: Grainger & Allison’s 5e, pp 668-675.


QUESTION 24
A 23-year-old woman complains of episodes of diarrhoea and rectal bleeding. Her father died of colorectal cancer aged 39. A double contrast barium enema is performed and demonstrates more than one hundred small polyps, measuring up to 5 mm in size, throughout the colon. An upper GI endoscopy demonstrates multiple polypoid lesions in the stomach and duodenum. What is the most likely diagnosis?
Carcinoid syndrome
Familial adenomatous polyposis
Hereditary non-polyposis colorectal cancer
Juvenile polyposis
Peutz-Jeghers syndrome
ANSWER: B
An autosomal dominant condition with multiple colonic adenomas and a 100% risk of colorectal carcinoma 20 years after diagnosis. Associated with hamartomas in the stomach, gastric and duodenal adenomas, and periampullary carcinoma.
References: Grainger & Allison’s 5e, pp 683-685; Chapman & Nakielny, Aids to Radiological Differential Diagnosis, pp 148-149.


QUESTION 25
A 78-year-old man has myelodysplastic syndrome and requires frequent blood transfusions. He develops progressively abnormal liver function tests and a grossly elevated ferritin level. An MRI of the liver is performed using breath hold half Fourier single shot spin echo T2w images. Which finding would make a diagnosis of haemosiderosis (iron overload from recurrent blood transfusion) more likely than haemochromatosis?
Increased T2 signal in the liver only
Increased T2 signal in the liver and spleen
Reduced T2 signal in the liver only
Reduced T2 signal in the liver and spleen
Reduced T2 signal in the spleen only
ANSWER: D
In iron overload due to recurrent transfusions, there is increased iron deposition in the reticuloendothelial system, leading to reduced T1, T2, and T2* signal intensity in the liver and spleen.
Reference: Martin DR, Danrad R, Hussain SM. MR imaging of the liver. Radiol Clin North Am 2005; 43(5):861-881.


QUESTION 26
A 31-year-old woman develops mild acute pancreatitis and is managed conservatively. It is her third episode of pancreatitis but there is no history of excess alcohol consumption and an abdominal ultrasound is normal. Magnetic resonance cholangiopancreatography (MRCP) is performed and is reported as showing evidence of pancreas divisum. Which one of the following findings is likely to have been present on MRCP?
A 3-cm cystic structure in the head of the pancreas
An accessory pancreatic duct passing around the duodenum
The common bile duct draining into the minor papilla
The dorsal pancreatic duct (duct of Santorini) draining into the minor papilla
The ventral pancreatic duct draining into the minor papilla
ANSWER: D
Relative stenosis of the cranially sited minor papilla results in an increased risk of pancreatitis in these patients.
Reference: Grainger & Allison’s 5e, pp 790-792.


QUESTION 27
A 47-year-old woman presents with a 2-day history of lower abdominal pain and reduced bowel habit. Dilated loops of small bowel are evident on an abdominal radiograph and a barium small bowel follow-through examination is performed. This demonstrates a stricture in a pelvic loop of small bowel. The patient’s symptoms improve on conservative management and further history reveals pelvic radiotherapy for cervical cancer 21 years ago. Which one of the following statements is true regarding radiation enteritis?
Acute symptoms following radiotherapy are a poor predictor of chronic enteritis.
The proximal jejunum is the most common site of small bowel involvement.
There is characteristic dilatation of affected small bowel in chronic radi-
There is flattening of the valvulae conniventes in the acute stage.
There is typically ‘cobblestoning’ of the small bowel mucosa.
ANSWER: A
Acute symptoms are not an accurate predictor of chronic radiation enteritis. The most common cause of radiation enteritis is pelvic radiotherapy for gynaecological malignancy or rectal cancer.
Reference: Chapman & Nakielny, Aids to Radiological Differential Diagnosis, pp 140-141.


QUESTION 28
A 22-year-old woman presents to her GP with a 4-month history of increasing right upper quadrant pain. An abdominal ultrasound is performed and demonstrates a 6-cm solid lesion of increased reflectivity in segment 6 of the liver. A contrast-enhanced CT of the liver is performed and demonstrates that the lesion enhances moderately and has a lobulated margin. Which additional finding would make a diagnosis of fibrolamellar carcinoma more likely than that of focal nodular hyperplasia (FNH)?
A hyperechoic central scar
A preexisting history of chronic liver disease
Delayed enhancement of a central scar
Punctuate calcification in the lesion
E) The patient is taking the combined oral contraceptive pill
ANSWER: D
There is considerable overlap in the imaging appearances of fibrolamellar carcinoma and focal nodular hyperplasia (FNH), but punctate calcification occurs in over half of patients with fibrolamellar carcinoma and is extremely unusual in FNH.
Reference: Grainger & Allison’s 5e, pp 739-749.



QUESTION 29
A 35-year-old woman is referred to the Radiology Department following the birth of her first child. The baby was delivered 8 days post-term and was a vaginal delivery following a prolonged labour and episiotomy. Two months later, the patient continues to experience faecal incontinence and an anal sphincter tear is suspected. Which investigation would be most useful to demonstrate anal sphincter damage?
Barium evacuation proctogram
CT colonography
CT with rectal contrast media
Endoanal ultrasound
MRI of the pelvis with a body coil
ANSWER: D
High-frequency endosonography allows an accurate assessment of the four layers of the anal wall: superficial and deep mucosa, submucosa, and muscularis propria.
Reference: Grainger & Allison’s 5e, pp 681-682, 703.


QUESTION 30
A 33-year-old woman presents to her GP with a one-year history of intermittent rectal bleeding. She experiences regular episodes of fresh blood per rectum with associated lower abdominal pain, lasting several days at a time. A flexible sigmoidoscopy is normal. A double contrast barium enema is performed and demonstrates an irregular appearance of the anterior wall of the sigmoid colon with mild extrinsic mass effect. What is the most likely diagnosis?
Carcinoma of the sigmoid colon
Endometriosis
Pelvic lipomatosis
Radiation enteritis
Solitary rectal ulcer syndrome
ANSWER: B
Involvement of the gastrointestinal tract is not uncommon in endometriosis, with the sigmoid colon and pelvic small bowel loops being typical sites of involvement.
Reference: Grainger & Allison’s 5e, p 701.


QUESTION 31
A 52-year-old man undergoes a thoracoabdominal oesophagectomy for squamous cell carcinoma of the mid oesophagus. The patient has an uncomplicated postoperative recovery and is discharged home. Four weeks later, a chest radiograph is performed. Which one finding would be unexpected on this chest radiograph?
Absence of right 5th rib posteriorly
Retrocardiac air-fluid level
Right paramediastinal soft tissue density mass
Moderate left hydropneumothorax
Vertical staple line in the mediastinum
ANSWER: D
Oesophagectomy may be performed by a transhiatal approach or thoracotomy, depending on the tumor’s location and the patient’s condition. A ‘neo-oesophagus’ may be formed by anastomosing the oesophageal remnant with the stomach, appearing as a paramediastinal soft tissue density mass on plain radiographs. The presence of a hydropneumothorax suggests anastomotic leakage.
Reference: Upponi S, Ganeshan A, Slater A, et al. Imaging following surgery for oesophageal cancer. Clin Radiol 2007; 62:724-731.


QUESTION 32
A 59-year-old man presents to his GP with a 3-day history of right upper quadrant pain and vomiting. There is a past medical history of ischaemic heart disease and type 2 diabetes mellitus. An abdominal ultrasound demonstrates thickening of the gallbladder wall and pericholecystic fluid, but no gallstones. The patient deteriorates clinically with elevation of white cell count and CRP levels. A repeat ultrasound 3 days later demonstrates a bright echogenic area in the gallbladder fundus with acoustic shadowing. What is the most likely diagnosis?
Adenomyomatosis
Emphysematous cholecystitis
Gallbladder carcinoma
Mirizzi syndrome
Porcelain gallbladder
ANSWER: B
The development of gas in the gallbladder of an unwell diabetic patient is suggestive of emphysematous cholecystitis.
Reference: Grainger & Allison’s 5e, pp 769-772.


QUESTION 33
A 48-year-old man presents to his GP with epigastric pain, diarrhoea, and weight loss over a period of 6 months. Laboratory investigations reveal a reduced serum albumin, and a contrast-enhanced CT of the abdomen demonstrates diffuse thickening of the gastric mucosa. A double contrast barium meal examination is performed and shows markedly thickened mucosal folds in the gastric body with sparing of the gastric antrum. The mucosal folds alter in size and position during the examination. What is the most likely diagnosis?
Eosinophilic gastritis
Gastric lymphoma
Infiltrative gastric adenocarcinoma (linitis plastica)
Menetrier’s disease
Organoaxial gastric volvulus
ANSWER: D
Menetrier’s disease characteristically produces thickened hyperplastic mucosa (sparing the gastric antrum), but the stomach remains pliable.
Reference: Grainger & Allison’s 5e, p 637.


QUESTION 34
A 46-year-old woman from Bangladesh is being treated for pulmonary tuberculosis. Despite anti-tuberculosis chemotherapy, she develops increasing fevers with abdominal discomfort and distension. An abdominal and pelvic ultrasound demonstrates a moderate volume of peritoneal free fluid, and a contrast-enhanced CT of the abdomen and pelvis is performed. What are the likely findings on CT?
A mixed solid:cystic ovarian mass with serosal deposits on the liver and spleen
Ascites with enlarged mesenteric lymph nodes containing high attenuation
Gastric wall thickening extending into the spleen with enlarged coeliac axis lymph nodes and ascites
Peritoneal nodularity with high density ascites
Portal vein thrombosis with ascites
ANSWER: D
In peritoneal tuberculosis, dense ascites, peritoneal nodularity, and lymph nodes with low attenuation centers are characteristic findings.
Reference: Grainger & Allison’s 5e, pp 712-714.


QUESTION 35
A 56-year-old woman presents to her GP with a 4-week history of lethargy and increasing jaundice. She is previously fit and well with no history of biliary or liver disease. An abdominal ultrasound is performed and demonstrates moderate intrahepatic biliary dilatation. Which feature in the patient’s medical history would significantly increase the risk of cholangiocarcinoma?
Drug history of regular nonsteroidal anti-inflammatory drug (NSAID) usage
Past medical history of giardiasis 2 years ago
Past medical history of ulcerative colitis
Jaundice associated with right upper quadrant pain
Patient allergic to iodinated contrast media
ANSWER: C
A history of inflammatory bowel disease is associated with a significantly increased risk of cholangiocarcinoma.
Reference: Grainger & Allison’s 5e, pp 781-782.


QUESTION 36
A 49-year-old man develops weight loss, upper abdominal pain, and three episodes of vomiting fresh red blood. Subsequent upper gastrointestinal endoscopy reveals a distal gastric adenocarcinoma. The patient undergoes a surgical procedure to resect the tumour, but develops increasing epigastric pain and fever 4 days later. An upper GI contrast study is performed. Which one of the following statements is true regarding this examination?
A partial distal gastrectomy with gastrojejunostomy (Billroth II procedure) involves an end-to-end anastomosis.
Control images prior to contrast administration are not indicated in this context.
If a water-soluble contrast examination appears normal, barium can be used as it has a higher sensitivity in identifying anastomotic leaks.
The oesophago-gastric junction is the most common site for perforation and contrast leaks.
Thickening of the mucosa at the surgical anastomosis with delayed gastric emptying is most likely due to residual gastric tumour.
ANSWER: C
Anastomotic leakage is one of the most serious complications following gastric surgery. In a contrast study, water-soluble contrast should be used initially, but if no leak is detected, barium can be used as it is more sensitive for detecting subtle postoperative leaks.
Reference: Woodfield CA, Levine MS. The postoperative stomach. Eur J Radiol 2005; 53:341-352.


QUESTION 37
A 47-year-old woman with obstructive jaundice undergoes an MRCP examination. This demonstrates a smooth stricture in the mid-common duct with associated moderate intrahepatic biliary dilatation. The stricture is caused by extrinsic compression from a round filling defect within the cystic duct. What is the diagnosis?
Acute bacterial cholangitis
Gallbladder carcinoma
Mirizzi syndrome
Postinflammatory biliary stricture
Primary sclerosing cholangitis (PSC)
ANSWER: C
In Mirizzi syndrome, a gallstone in the cystic duct produces mass effect on the common duct and can lead to fistula formation.
Reference: Grainger & Allison’s 5e, pp 777-779.



QUESTION 38
A 56-year-old woman presents with a 4-day history of right upper quadrant pain and vomiting. She describes a previous episode one year ago that resolved after a few days. On examination, she is very tender in the right upper quadrant with guarding on deep palpation during inspiration. Laboratory investigations reveal elevated white cell count and CRP but normal liver function tests and an abdominal ultrasound is performed. What are the most likely ultrasound findings?
Hypoechoic mass in the pancreatic head with common bile duct measuring 14 mm and pancreatic duct measuring 6 mm in diameter
Nodular liver surface, mixed reflectivity liver texture and ascites
Severe intrahepatic duct dilatation with no cause identified
Several large gallstones with gallbladder wall measuring 5 mm and a rim of pericholecystic fluid
Several small gallstones with gallbladder wall thickness of 2 mm
ANSWER: D
Ultrasound findings of acute cholecystitis include gallbladder distension and the sonographic Murphy’s sign. Normal gallbladder wall thickness may be up to 3 mm, with thickening potentially due to non-biliary causes.
Reference: Chapman & Nakielny, Aids to Radiological Differential Diagnosis, p 171.


QUESTION 39
A 42-year-old man is admitted to hospital with acute abdominal pain. There is a significant medical history of polycythaemia rubra vera, for which the patient undergoes regular venesection. On examination, there is right upper quadrant tenderness and hepatomegaly. Liver function tests are acutely elevated and the patient’s condition deteriorates. A catheter angiogram is performed to assess the major hepatic vessels and shows a ‘spider’s web’ appearance within the liver. What is the diagnosis?
Budd Chiari syndrome
Capillary haemangioma
Hereditary haemorrhagic telangiectasia (HHT)
Portal vein thrombosis
Spontaneous hepatic haematoma
ANSWER: A
When contrast is injected into the hepatic veins, a ‘spider’s web’ appearance of collateral vessels is diagnostic of Budd-Chiari syndrome.
Reference: Grainger & Allison’s 5e, pp 751-755.


QUESTION 40
A 74-year-old woman is referred to the hepatology outpatient clinic with persistently abnormal liver function tests. There is a past medical history of myocardial infarction, atrial fibrillation and hypertension, but no previous history of liver disease. On abdominal ultrasound, the liver appears normal with antegrade portal venous flow demonstrated. A CT of the abdomen is performed and the mean density of the liver is 86 Hounsfield Units (HU) precontrast. What is the most likely diagnosis?
Amiodarone therapy
Chronic Budd Chiari syndrome
Chronic hepatitis B
Diffuse fatty infiltration
Wilson’s disease
ANSWER: A
Amiodarone contains iodine; its deposition in the liver leads to increased density on CT.
References: Grainger & Allison’s 5e, p 733; Chapman & Nakielny, Aids to Radiological Differential Diagnosis, p 175.


QUESTION 41
A 68-year-old man presents to his GP with weight loss and jaundice. Liver function tests demonstrate obstructive jaundice and an abdominal ultrasound shows mild intrahepatic biliary dilatation with a common bile duct measuring 12 mm in diameter. In the pancreatic head, a 3-cm hypoechoic mass is present. An ERCP is performed with insertion of a plastic stent and brushings confirm a pancreatic ductal adenocarcinoma. A triple-phase (precontrast, arterial and portal venous) multidetector CT of the pancreas is performed. Which finding would indicate a nonresectable pancreatic tumour?
Enhancing pancreatic parenchyma between the tumour and superior mesenteric artery
The pancreatic duct dilated to 6 mm
The presence of a 5-mm coeliac axis lymph node
The tumour has invaded the duodenum
The tumour in contact with 75% of the superior mesenteric artery
ANSWER: E
If the tumor is in contact with more than half of the vessel circumference, it is very unlikely to be resectable.
Reference: Grainger & Allison’s 5e, pp 801-803.


QUESTION 42
An 82-year-old woman is referred to the on-call surgical team as an emergency admission. The patient lives in a residential care home and has a 48-hour history of generalised abdominal pain and vomiting. On examination, she is dehydrated and tachycardic and an abdominal radiograph demonstrates multiple dilated small bowel loops measuring up to 4.8 cm in diameter. A linear gas-filled structure is present in the right upper quadrant with short branches extending from it. What is the most likely diagnosis?
Acute mesenteric ischaemia
Emphysematous cholecystitis
Gallstone ileus
Obstructed right inguinal hernia
Small bowel obstruction due to adhesions
ANSWER: C
A gallstone causing a cholecystoduodenal fistula can lead to aerobilia and obstruct the distal small bowel.
Reference: Grainger & Allison’s 5e, p 771.


QUESTION 43
A 72-year-old man presents with a 3-month history of significant weight loss, upper abdominal pain and pruritus. On examination, the patient is clinically jaundiced and cachectic. A contrast-enhanced CT of the abdomen demonstrates marked intrahepatic biliary dilatation, a dilated common bile duct and a mass in the pancreatic head. An attempted ERCP fails as the ampulla of Vater cannot be cannulated. The patient attends the Radiology Department for percutaneous biliary drainage. Which one of the following statements is true?
Biliary sepsis is an absolute contraindication to percutaneous biliary drainage.
Excessive contrast injection into the intrahepatic ducts is a recognised cause of septic shock.
If a malignant stricture is potentially resectable, a metallic biliary stent should be inserted.
Percutaneous transhepatic cholangiography (PTC) is performed under general anaesthesia in the majority of cases.
Prophylactic antibiotics are not routinely used in PTC.
ANSWER: B
Care should be taken not to overfill the intrahepatic ducts as this can lead to hemodynamic instability. Biliary sepsis is a relative contraindication to percutaneous transhepatic cholangiography (PTC), but drainage may be needed in obstructed and infected biliary systems.
Reference: Chapman S, Nakielny R. A Guide to Radiological Procedures, 4th edition (Edinburgh: Saunders, 2003), pp 115-121.


QUESTION 44
A 47-year-old man is knocked off his motorcycle and brought to the Emergency Department. On examination, he is haemodynamically stable but has left upper quadrant tenderness. A contrast-enhanced CT of the abdomen is performed and shows no evidence of visceral injury. The reporting radiologist notices a solitary, well-defined lesion in the large bowel that is of lower attenuation than the surrounding colonic wall. Which single additional finding would be most consistent with a colonic lipoma?
There is a mean density of —10 HU on CT.
Mucosal ulceration is seen on colonoscopy.
On ultrasound, the lesion changes shape when compressed.
The lesion lies in the sigmoid colon.
There is a one-month history of rectal bleeding and weight loss.
ANSWER: C
Known as the 'squeeze sign’.
Reference: Grainger & Allison’s 5e, p 700.


QUESTION 45
A 31-year-old woman has a 6-month history of intermittent right upper quadrant pain. An abdominal ultrasound examination is performed and reveals a 3-cm hyperechoic mass in segment 6 of the liver. She undergoes an MRI examination of the liver with intravenous gadolinium. On the precontrast T1-weighted images, the signal intensity of the lesion is isointense to surrounding liver parenchyma. Which one of the following statements is true regarding the post-gadolinium T1-weighted images?
Focal fatty infiltration demonstrates enhancement in the arterial phase.
HCC usually enhances in the delayed phase images only.
Hepatic adenomas typically demonstrate uniform enhancement in the arterial phase.
Hypervascular metastases are typically hyperintense on T1 precontrast.
Progressive centripetal enhancement in the portal venous and delayed phases is seen with HCC.
ANSWER: C
Hepatic adenoma, HCC, and focal nodular hyperplasia typically show marked enhancement in the arterial phase. Hypervascular liver metastases are usually hypointense on T1 and hyperintense on T2. The characteristic behavior of a liver hemangioma—not HCC—is described in option E.
Reference: Yu SCH, Yeung DTK, So NMC. Imaging features of hepatocellular carcinoma. Clin Radiol 2004; 59:145-156.


QUESTION 46
A 32-year-old man attends the Emergency Department 2 hours after he was assaulted outside a nightclub. On examination, he is haemodynamically stable with abrasions and tenderness over the lower left chest. The patient reports that he sustained significant abdominal injuries following an assault 7 years ago. A contrast-enhanced CT of the chest and abdomen is performed and demonstrates a fracture of the left 10th rib, but no intrathoracic injury. There is no visible spleen but multiple small nodules of uniformly enhancing soft tissue are present in the left upper quadrant and extend to the left iliac fossa. No peritoneal free fluid is demonstrated. What is the most likely diagnosis?
Asplenia
Polysplenia
Shattered spleen
Splenosis
Wandering spleen
ANSWER: D
Previous splenic injury can lead to autotransplantation of splenic tissue onto serosal surfaces within the abdomen.
Reference: Grainger & Allison’s 5e, pp 1761-1769.


QUESTION 47
A 52-year-old man has a 3-year history of dysphagia and heartburn. There is no history of haematemesis and the patient’s weight is stable. A barium swallow is performed and demonstrates a smooth narrowing of the mid-oesophagus. Small, saccular projections of barium are seen at the level of the stricture, extending perpendicular to the oesophagus. What is the cause of this appearance?
Aphthous ulceration
Candida albicans plaques
Epiphrenic pulsion diverticulae
Infiltration by adjacent non-small cell lung cancer
Intramural pseudodiverticulosis
ANSWER: E
This rare condition is secondary to chronic inflammation causing dilated excretory ducts (‘flask-shaped’ projections of barium) in the oesophageal wall.
Reference: Grainger & Allison’s 5e, p 624.


QUESTION 48
A 38-year-old woman presents to her GP with a 3-month history of lethargy, nausea and itching. She was diagnosed with ulcerative colitis 8 years ago and has been treated with short courses of steroids and long-term oral mesalazine. Blood tests demonstrate an elevated serum bilirubin with markedly high alkaline phosphatase. MRCP demonstrates multiple biliary strictures with small diverticulae arising from the common duct. Which statement is true regarding the underlying diagnosis?
Ten to 20% of patients have inflammatory bowel disease.
Cessation of anti-inflammatory medication leads to normalisation of liver function tests.
It is also known as the type 5 choledochal cyst.
Only the extrahepatic biliary ducts are involved.
There is a significant increased risk of cholangiocarcinoma.
ANSWER: A
Necrotic pancreatic tissue will demonstrate reduced or absent enhancement on contrast-enhanced CT. The presence of gas is a strong predictor of infection. Local vascular complications may occur in severe acute pancreatitis without pancreatic necrosis.
Reference: Saokar A, Rabinowitz CB, Sahani DV. Cross-sectional imaging in acute pancreatitis. Radiol Clin North Am 2007; 45(3):447-460.



QUESTION 49
A 27-year-old woman is referred to the gastroenterology outpatient clinic with a 3-month history of upper abdominal pain. There is no past medical history of note, but her sister has recently been diagnosed with a ‘brain tumour’. A contrast-enhanced CT (portal venous phase) of the abdomen demonstrates a multicystic lesion in the head of the pancreas. The lesion contains 10 cysts measuring up to 15 mm in size with a small amount of calcification centrally. Several larger cysts are present in the pancreatic body and tail, and both kidneys contain cortical cysts. What is the most likely underlying diagnosis?
Autosomal dominant polycystic kidney disease
Cystic fibrosis
HHT
Tuberous sclerosis
Von Hippel Lindau disease (VHL)
ANSWER: E
The cystic pancreatic lesion is likely to be a serous cystadenoma, and in combination with simple pancreatic and renal cysts, is consistent with von Hippel-Lindau syndrome (VHL).
Reference: Grainger & Allison’s 5e, pp 792, 804.



QUESTION 50
A 38-year-old woman presents to her GP with a 3-month history of lethargy, nausea, and itching. She was diagnosed with ulcerative colitis 8 years ago and has been treated with short courses of steroids and long-term oral mesalazine. Blood tests demonstrate an elevated serum bilirubin with markedly high alkaline phosphatase. MRCP demonstrates multiple biliary strictures with small diverticulae arising from the common duct. Which statement is true regarding the underlying diagnosis?
Ten to 20% of patients have inflammatory bowel disease.
Cessation of anti-inflammatory medication leads to normalization of the liver function tests.
It is also known as the type 5 choledochal cyst.
Only the extrahepatic biliary ducts are involved.
There is a significant increased risk of cholangiocarcinoma.
ANSWER: E
Up to 10% of patients with primary sclerosing cholangitis will develop cholangiocarcinoma.
Reference: Grainger & Allison’s 5e, pp 777-778.



QUESTION 51
A 66-year-old man undergoes screening for colorectal cancer and is found to have two positive stool samples for faecal occult blood. The patient is asymptomatic with no significant medical history. He is referred for CT colonography (CTC). Which one of the following statements is correct regarding CTC?
As much as 0.5–1% of examinations result in colonic perforation.
A routine examination should involve supine imaging only.
Significant extracolonic pathology is identified in 30-40% of symptomatic patients.
The administration of intravenous contrast (portal venous imaging) is advised for asymptomatic patients, as it improves the detection of colonic lesions.
The use of an antispasmodic (e.g., Buscopan) immediately prior to gas insufflation enables optimal colonic distension.
ANSWER: E
CT colonography (CTC) is generally safe with a reported perforation rate in symptomatic patients of 0.03%. Supine and prone imaging is recommended to maximize colonic distension, and the use of an antispasmodic is advised to avoid colonic spasm. There is no strong evidence that intravenous contrast improves colonic lesion detection, but it may help assess extracolonic pathology.
Reference: Tolan DJM, Armstrong EM, Burling D, et al. Optimization of CT colonography technique: a practical guide. Clin Radiol 2007; 62:819-827.


QUESTION 52
A 71-year-old woman is referred to the on-call surgical team as an emergency admission. She complains of a 1-week history of lower abdominal pain, nausea, and vomiting. She has passed loose bowel motions over the past 2 days with no bleeding per rectum. She experienced a similar, less severe, episode of lower abdominal pain 2 years ago that resolved spontaneously. On examination, the patient is pyrexial and tender in the left iliac fossa. Blood tests reveal elevated inflammatory markers and white cell count. What would be the most likely findings on a contrast-enhanced CT?
A thickened segment of sigmoid colon with mesenteric stranding and a small pericolonic fluid collection.
Annular thickening of the sigmoid colon with several enlarged local lymph nodes.
Areas of wall thickening throughout the colon with fistulous tracts between bowel loops.
Extensive pneumoperitoneum.
Extensive wall thickening of the rectum, sigmoid, and descending colon with minimal pericolonic stranding.
ANSWER: A
The history is typical of acute diverticulitis. These CT findings would be consistent with ‘moderate’ diverticulitis with a small pericolonic abscess.
Reference: Grainger & Allison’s 5e, pp 690-692.


QUESTION 53
An 80-year-old man is referred to the gastroenterology outpatient clinic with a 1-year history of dysphagia. He describes worsening difficulty swallowing solids and liquids with associated loss of 3 kg in weight. The past medical history includes Parkinson’s disease and right lower lobe pneumonia 6 months ago. An upper gastrointestinal endoscopy is normal, and the patient is referred for a contrast swallow examination for suspected oesophageal dysmotility. Which statement is true regarding this examination?
If aspiration is suspected, water-soluble meglumine diatrizoate (Gastrografin) should be used initially.
In suspected oesophageal dysmotility, an antispasmodic (e.g., Buscopan) should be administered prior to prone swallow.
Motility of the mid- and lower oesophagus is best assessed with the patient standing erect in the left anterior oblique position.
Repeated swallowing should be avoided, and only single boluses of barium should be used to assess for oesophageal dysmotility.
Secondary oesophageal contractions are chaotic and do not propel the barium bolus.
ANSWER: D
Repeated swallowing can interrupt normal peristalsis and produce a falsely abnormal appearance.
Reference: Grainger & Allison’s 5e, pp 610-611.


QUESTION 54
A 72-year-old man is referred to hospital as an emergency admission by his GP. He has experienced vomiting and abdominal pain for 24 hours following a takeaway meal. There is a past medical history of ischaemic heart disease, chronic obstructive pulmonary disease, and hypertension. An abdominal radiograph is performed and demonstrates several gas-filled loops of small bowel centrally measuring up to 2.5 cm in diameter. In the left side of the abdomen, multiple round foci of gas are projected over the wall of a loop of large bowel. No free gas or mucosal thickening is identified. What is the most likely explanation for the clinical and radiographic findings?
Gastroenteritis with incidental pneumatosis coli.
Emphysematous pyelonephritis with a paralytic ileus.
Ischaemic colitis causing intramural bowel gas.
Perforated sigmoid diverticulitis with gas in the retroperitoneum.
Small bowel obstruction due to a gallstone ileus.
ANSWER: A
The presence of cyst-like gas pockets in the left hemicolon of a patient with COPD is suggestive of pneumatosis cystoides intestinalis (pneumatosis coli).
Reference: Grainger & Allison’s 5e, pp 599-601.


QUESTION 55
A 68-year-old woman presents with a 2-month history of generalised abdominal bloating and two episodes of vaginal bleeding. On examination, the abdomen is distended with clinical evidence of ascites. Tumour markers are performed; CA 15-3 is normal, CA 125 and CEA are slightly elevated, and CA 19-9 is markedly elevated. An abdominopelvic ultrasound demonstrates a moderate volume of ascites, multiple liver metastases, and bilateral mixed solid/cystic adnexal masses. What is the most likely underlying primary tumour?
Breast cancer
Gastric adenocarcinoma
Melanoma
Ovarian cancer
Primary peritoneal carcinoma
ANSWER: B
This clinical history is classic for a Krukenberg tumor—ovarian metastases from a GI tumor (most frequently gastric adenocarcinoma). Colorectal cancer is the second most common cause of this type of metastatic tumor presentation.
Reference: Yada-Hashimoto M, Yamato T, Kamiura S, et al. Metastatic ovarian tumors: a review of 64 cases. Gynecol Oncol 2003; 89(2):314-317.


QUESTION 56
A 30-year-old male patient arrives at the Radiology Department for a barium follow-through examination. He has experienced chronic lower abdominal pain with weight loss and intermittent diarrhoea. Optical colonoscopy was normal. As the Specialist Registrar in the department, it is your responsibility to supervise this investigation, and the radiographer asks how you would like the examination performed. Which statement is true regarding the barium follow-through examination?
A 250% weight-to-volume barium sulphate should be used.
Barium reaches the caecum within 30 minutes in the majority of patients.
Barium sulphate suspensions are nonionic to avoid clumping of particles.
Oral metoclopramide may be used to delay gastric emptying.
The first radiograph should be a supine film after 60 minutes.
ANSWER: C
Barium sulfate preparations consist of tiny particles (less than 1 µm) in a nonionic suspension.
References: Grainger & Allison’s 5e, p 660; Chapman & Nakielny, A Guide to Radiological Procedures, 4th edition (Edinburgh: Saunders, 2003), pp 62-64.


QUESTION 57
A 53-year-old man is seen in the liver transplant outpatient clinic. Two years ago, he underwent an orthotopic liver transplant for alcoholic liver disease and currently takes oral cyclosporin. He reports a 3-month history of weight loss and his liver function tests are found to be abnormal. A contrast-enhanced CT demonstrates multiple new low attenuation lesions within the liver. There is also marked thickening of several small bowel loops. What is the most likely diagnosis?
Chronic graft ischaemia with portal hypertension
Cyclosporin hepatotoxicity
Multifocal hepatocellular carcinoma
Post transplant lymphoproliferative disorder (PTLD)
Secondary amyloidosis
ANSWER: D
Up to 5% of liver transplants develop post-transplant lymphoproliferative disorder (PTLD); extranodal disease is the most common pattern.
Reference: Grainger & Allison’s 5e, p 1754.


QUESTION 58
A 29-year-old woman received a living related bone marrow transplant for chronic myeloid leukaemia 13 days ago. She has experienced bloody diarrhoea and severe lower abdominal pain for the past 4 days, and an abdominal radiograph demonstrates prominent loops of gas-filled large bowel. A contrast-enhanced CT of the abdomen is performed and shows moderate wall thickening of the right hemicolon and terminal ileum with mesenteric fat stranding. There is no abdominal lymphadenopathy and the rectum and sigmoid colon appear normal. What is the most likely diagnosis?
Crohn’s disease
Cytomegalovirus (CMV) colitis
Neutropenic colitis
PTLD
Pseudomembranous colitis
ANSWER: C
The patient is likely to be severely neutropenic, and the CT findings are typical of neutropenic colitis.
Reference: Grainger & Allison’s 5e, p 698.


QUESTION 59
A 33-year-old man presents to his GP with a 6-month history of increasing epigastric pain and vomiting. An upper GI endoscopy demonstrates multiple small ulcers in the gastric antrum and first and second parts of the duodenum. Biopsies show benign ulceration and are negative for Helicobacter pylori. The patient’s symptoms do not improve on a high-dose oral proton pump inhibitor, and an abdominal ultrasound demonstrates a well-defined 2-cm hypoechoic lesion in the pancreatic head. Which statement is true regarding the most likely underlying diagnosis?
Ten to 20% of the pancreatic lesions are malignant
The condition is part of the type 2 multiple endocrine neoplasia syndrome
The pancreatic lesion is solitary in 80–90% of cases
The pancreatic lesion will enhance avidly on contrast-enhanced CT
There will be flattening of duodenal folds on a double contrast barium examination
ANSWER: D
The clinical and imaging findings are highly suggestive of Zollinger-Ellison syndrome (hyperacidity due to an underlying gastrinoma).
Reference: Grainger & Allison’s 5e, p 804.


QUESTION 60
A 32-year-old man with Crohn’s disease reports increased perianal pain and swelling over a 2-month period. On examination, there is a small perineal sinus lying at the 3 o’clock position in relation to the anus. On MRI, a fistulous track of high T2 signal is seen to pass from the anal canal, through the internal sphincter, and then runs medial to the external sphincter. The track reaches the skin surface of the perineum and correlates with the sinus opening on physical examination. Which description best describes this anal fistula?
Extrasphincteric
Infrasphincteric
Intersphincteric
Suprasphincteric
Trans-sphincteric
ANSWER: C
The Parks’ classification defines anal fistulae by the structures involved. The intersphincteric fistula is the most common (around 70%) and does not pass through the external sphincter.
Reference: Grainger & Allison’s 5e, pp 703-704.


QUESTION 61
A 32-year-old woman undergoes a laparoscopic cholecystectomy for gallstones. Seven days later, she presents to the Emergency Department with increasing abdominal pain and fevers. On examination, her temperature is 39.6°C, HR = 100 bpm, and BP = 110/60 mmHg with tenderness and guarding in the right upper and lower quadrants of the abdomen. Laboratory investigations reveal a grossly elevated CRP level and white cell count. The clinical team requests a contrast-enhanced CT for suspected intra-abdominal sepsis. Which statement is true regarding intra-abdominal fluid collections?
Fluid in the lesser sac communicates freely with the left subphrenic space.
Fluid in the right paracolic gutter communicates freely into the pelvis and superiorly to the right subdiaphragmatic space.
Fluid in the right paracolic gutter will be bounded superiorly by the phrenicocolic ligament.
Postoperative gallbladder collections usually lie in the right infracolic space.
The right subphrenic space is also called ‘Morrison’s pouch’.
ANSWER: B
The right paracolic gutter communicates freely with the right perihepatic space. Postoperative gallbladder collections will tend to lie in the gallbladder fossa and the hepatorenal recess (Morrison’s pouch).
Reference: Grainger & Allison’s 5e, pp 707-708.


QUESTION 62
A 79-year-old man is brought to the Emergency Department with generalised abdominal pain and vomiting for 5 days. He has not opened his bowels or passed flatus during this period and has been immobile for the past 48 hours. On examination, he is dehydrated with a distended abdomen and increased bowel sounds. An abdominal radiograph is performed and shows dilated loops of large bowel, measuring up to 5 cm in diameter. Dilated small bowel is present centrally, but there is no evidence of perforation. Which statement is true regarding this clinical setting?
Colonic pseudo-obstruction is a recognised cause of these radiographic findings.
Diverticulitis is the most common cause of large bowel obstruction in the UK.
Obstruction of the large bowel occurs more commonly on the right side of the colon than the left.
Paralytic ileus is excluded by these radiographic findings.
The ileocaecal valve is not competent in this patient.
ANSWER: A
Colonic pseudo-obstruction can produce the same radiographic findings as large bowel obstruction; an instant contrast enema or CT should differentiate between mechanical obstruction and pseudo-obstruction.
Reference: Grainger & Allison’s 5e, pp 595–596.



QUESTION 63
A 17-year-old man has a 2-month history of abdominal pain and rectal bleeding. Clinical examination is unremarkable and a flexible sigmoidoscopy is normal. A Tc-99m pertechnetate study is performed, demonstrating abnormal activity in the lower abdomen. One month later, the patient presents to the Emergency Department with acute abdominal pain and vomiting. A contrast-enhanced CT of the abdomen shows an ileocolic intussusception. What is the most likely underlying diagnosis?
Colonic lipoma
Crohn’s disease
Meckel’s diverticulum
Small bowel adenocarcinoma
Whipple’s disease
ANSWER: C
In adults, a minority of Meckel’s diverticula contain gastric mucosa and can lead to gastrointestinal bleeding. The diverticulum may also become inverted and act as a ‘lead point’ for an intussusception.
References: Grainger & Allison’s 5e, p 674; Chapman & Nakielny, Aids to Radiological Differential Diagnosis, p 160.


QUESTION 64
A 27-year-old man is referred to the hepatology outpatient clinic with a 3-week history of malaise, lethargy, and mild upper abdominal pain. Liver function tests performed by his GP are significantly abnormal. The results of hepatitis serology performed in the clinic are consistent with an acute hepatitis B infection. An abdominal ultrasound is performed. What is the most likely finding on ultrasound?
Decreased reflectivity of the liver parenchyma
Increased reflectivity of the liver parenchyma
Nodular liver surface
Normal ultrasound appearances
Retrograde portal venous flow
ANSWER: D
In acute viral hepatitis, there can be diffusely reduced reflectivity of the liver, but the majority of patients have a normal ultrasound examination.
Reference: Grainger & Allison’s 5e, p 733.


QUESTION 65
A 49-year-old woman is an emergency admission to the surgical admissions unit with a 5-day history of upper abdominal pain. On clinical examination, there is right upper quadrant tenderness and laboratory investigations show an elevated white cell count and CRP. An abdominal ultrasound is performed, but is of limited value due to the patient’s body habitus and the gallbladder is poorly visualised. The patient undergoes dynamic radioisotope hepatobiliary scintigraphy with an intravenous injection of a Tc-99m-labelled pharmaceutical. Which one of the following statements is true regarding radioisotope hepatobiliary scintigraphy?
Increased isotope activity in the region of the gallbladder is consistent with acute cholecystitis.
Nonvisualisation of the gallbladder after 2 hours is consistent with acute cholecystitis.
Sulphur colloid is the most commonly used pharmaceutical in this procedure.
The administration of intravenous morphine causes sphincter of Oddi relaxation.
Visualisation of isotope activity in the duodenum is abnormal.
ANSWER: B
The normal gallbladder will appear after approximately 20 minutes. In acute cholecystitis, the gallbladder is typically not seen due to cystic duct obstruction.
References: Grainger & Allison’s 5e, p 769; Chapman & Nakielny, A Guide to Radiological Procedures, 4th edition (Edinburgh: Saunders, 2003), pp 127-131.


QUESTION 66
A 79-year-old woman trips and falls whilst stepping off a bus. She suffers a fractured right neck of femur and undergoes a hemiarthroplasty the following day. Her early recovery is complicated by bronchopneumonia which resolves after 5 days of broad spectrum antibiotics. On her tenth day in hospital, she develops abdominal pain and diarrhoea and pseudomembranous colitis is suspected clinically. Which one of the following statements is true regarding pseudomembranous colitis?
A normal abdominal CT effectively excludes pseudomembranous colitis.
Ascites is present in up to 40% of patients.
CT carries a low positive predictive value for pseudomembranous colitis.
Extensive pericolonic stranding is a typical feature on CT.
The rectum is not involved in 40–50% of patients.
ANSWER: B
Ascites can occur with other colitides but is often seen in pseudomembranous colitis. CT typically demonstrates mucosal enhancement and marked colonic wall thickening with only mild pericolonic stranding in patients with pseudomembranous colitis. These findings have a high positive predictive value, but a normal CT does not exclude pseudomembranous colitis. Rectal sparing occurs in around 10% of patients.
Reference: Ramachandran I, Sinha R, Rodgers P. Pseudomembranous colitis revisited: spectrum of imaging findings. Clin Radiol 2006; 61:535-544.


QUESTION 67
A 63-year-old man attends the Radiology Department for an MRCP. He was recently found to have abnormal liver function tests and an abdominal ultrasound showed multiple stones in the gallbladder with a dilated common bile duct. The surgical team has requested the MRCP to assess whether there are gallstones in the bile ducts. Which statement is true regarding MRCP in this setting?
Blood in the biliary tree is a recognised cause of a false positive MRCP.
MRCP diagnostic quality reduces as the serum bilirubin rises.
MRCP is reliant on contrast excretion into the biliary tree.
The sensitivity of MRCP for choledocholithiasis is 60–70%.
The sequences are heavily T1 weighted in the majority of cases.
ANSWER: A
Gas, blood, or flow voids can all produce filling defects in the biliary tree on MRCP.
Reference: Grainger & Allison’s 5e, pp 766, 775-777.


QUESTION 68
A 45-year-old man undergoes an upper GI endoscopy following a 2-month history of weight loss and dysphagia to solids. The endoscopy demonstrates a tumour in the mid-oesophagus and biopsies confirm a squamous cell carcinoma. An endoscopic ultrasound is subsequently performed and demonstrates a hypoechoic tumour mass in the anterior aspect of the mid-oesophagus. The tumour is seen to infiltrate the muscularis propria and extends beyond the serosal surface of the oesophagus. Which structure is most at risk of direct invasion by this oesophageal tumour?
Azygos vein
Left lobe of liver
Left main bronchus
Right diaphragmatic crus
Right ventricle
ANSWER: C
The mid-oesophagus has the heart, pericardium, and left main bronchus as its key anterior relations.
Reference: Grainger & Allison’s 5e, p 609.


QUESTION 69
A 51-year-old man attends the Emergency Department with a 3-hour history of sudden onset lower abdominal pain and vomiting. On examination, there is tenderness in the right iliac fossa but laboratory investigations are remarkable only for a mildly elevated CRP level. A contrast-enhanced CT of the abdomen is performed and demonstrates an ovoid mass lying medial to the caecum with high attenuation stranding in the pericolic fat and a central area of low density (−150 HU). There is no colonic wall thickening identified. What is the diagnosis?
Acute appendicitis
Epiploic appendagitis
Ileocaecal tuberculosis
Meckel’s diverticulum
Right-sided diverticulitis
ANSWER: B
Torsion of an epiploic appendage leads to sudden onset of localized pain with characteristic CT findings of a pericolic inflammatory mass with central fat density.
Reference: Grainger & Allison’s 5e, p 692.


QUESTION 70
A 67-year-old man is referred to the gastroenterology outpatient clinic with a 6-week history of upper abdominal pain, vomiting, and weight loss. The patient has previously been fit and well but has lost 10 kg in weight during this period. Clinical examination and laboratory investigations are unremarkable. A contrast-enhanced CT of the abdomen is performed and demonstrates extensive thickening of the gastric body and antrum. Which additional feature would make a diagnosis of gastric carcinoma more likely than gastric lymphoma?
Direct invasion of the left lobe of liver
Coeliac axis lymphadenopathy
Preserved perigastric fat planes
Previous Helicobacter pylori infection
Regional lymphadenopathy
ANSWER: A
Advanced gastric carcinoma is far more likely to directly invade local structures and obliterate the perigastric fat planes.
Reference: Grainger & Allison’s 5e, pp 646-648.


QUESTION 71
A 62-year-old woman presents to the Emergency Department with a 2-day history of excruciating abdominal pain and is found to have an elevated serum amylase. An abdominal ultrasound demonstrates multiple stones in the gallbladder but there is no biliary dilatation and the pancreas is obscured by bowel gas. The patient’s clinical condition deteriorates and a contrast-enhanced CT is performed. This demonstrates ill-defined enlargement of the pancreas with infiltration of the peripancreatic fat. The peripancreatic fluid is localized only to the anterior pararenal space. Which one other structure also lies in the anterior pararenal space?
Descending colon
Gallbladder
Kidneys
Spleen
Stomach
ANSWER: A
The anterior pararenal space is the most anterior of the three retroperitoneal compartments.
Reference: Grainger & Allison’s 5e, p 790.


QUESTION 72
A 35-year-old man has a history of excess alcohol intake and is referred for an abdominal ultrasound by his GP. This demonstrates a 3-cm area of increased reflectivity within liver segment 4a. The lesion does not have any mass effect on adjacent vessels and has a geographic margin. A diagnosis of focal fat deposition is suspected and an MRI of the liver is performed. Which MRI artefact can be utilized to confirm this diagnosis?
Aliasing
Chemical shift
Magic angle
Susceptibility
Truncation
ANSWER: B
In- and out-of-phase sequences utilize chemical shift artifact. Fat deposition in the liver will show a significant reduction in signal during the out-of-phase images.
Reference: Grainger & Allison’s 5e, pp 95-98, 743.


QUESTION 73
A 40-year-old woman has a 15-year history of ulcerative colitis (UC). After the initial diagnosis, she suffered frequent exacerbations of colitis requiring several hospital admissions. She declined surgical intervention at that stage and has subsequently been well controlled on medical management. Recently, she has developed a change in bowel habit and a double contrast barium enema is performed. This shows a stricture in the descending colon. Which one statement is true regarding strictures in ulcerative colitis?
Abrupt shouldering is typical of a benign stricture in UC.
In patients with UC, colorectal carcinomas typically arise from tubular adenomas.
The majority of strictures in UC are benign.
There is no increased risk of colorectal carcinoma in patients with UC.
Widening of the presacral space is pathognomonic of a rectal carcinoma.
ANSWER: C
Benign strictures in ulcerative colitis are typically smooth and symmetrical and result from chronic smooth muscle hypertrophy. These occur in 10-20% of patients with ulcerative colitis and are most common in the left colon. Carcinomas arise from dysplastic changes within the diseased epithelium, not from adenomas as in the general population.
Reference: Grainger & Allison’s 5e, pp 696, 699-700.



QUESTION 74
A 17-year-old man is referred to the gastroenterology outpatient clinic with iron deficiency anaemia. The patient is otherwise well with no gastrointestinal symptoms and a normal physical examination. Endoscopic examination of the upper and lower gastrointestinal tract is normal. A mesenteric catheter angiogram is performed and demonstrates a persistent vitelline artery. What is the diagnosis?
Behçet’s disease
Colonic arteriovenous malformation
Intestinal lymphangiectasia
Meckel’s diverticulum
Small bowel angiodysplasia
ANSWER: D
This angiographic finding is diagnostic of a Meckel’s diverticulum, indicating that a remnant of the omphalomesenteric (vitelline) duct is present.
Reference: Grainger & Allison’s 5e, p 674.


QUESTION 75
An 81-year-old man presents with a 3-month history of weight loss and upper abdominal pain. Serum amylase is normal but CA 19-9 is elevated and liver function tests are abnormal. An abdominal ultrasound demonstrates mild intrahepatic biliary dilatation with the common bile duct measuring 16 mm in diameter. The pancreatic head is obscured by bowel gas and a contrast-enhanced CT of the abdomen is performed. What is the most likely finding in the pancreas?
A 1-cm intensely enhancing mass in the pancreatic body
A 6-cm septated cyst in the pancreatic tail
Diffusely enlarged pancreas with peripancreatic fluid collection
Hypovascular mass in the pancreatic head
Pancreatic ductal calcification and atrophy
ANSWER: D
The history of elevated CA 19-9 and obstructive jaundice is highly suggestive of a pancreatic ductal adenocarcinoma. The classic CT appearance of pancreatic ductal adenocarcinoma is a hypovascular mass with pancreatic and/or bile duct dilatation. Using a pancreatic mass protocol, these typical CT findings have a high positive predictive value and can help to differentiate ductal adenocarcinoma from other pancreatic masses (focal pancreatitis, neuroendocrine tumors, etc).
Reference: Amin Z, Theis B, Russell RCG, et al. Diagnosing pancreatic cancer: the role of percutaneous biopsy and CT. Clin Radiol 2006; 61:996-1002.


QUESTION 76
A 74-year-old man attends the Radiology Department for an abdominal ultrasound examination. He has a 2-month history of nausea and vomiting with unexplained weight loss. On ultrasound, there are linear structures of high reflectivity seen within liver segments 2-4. On turning into the left lateral decubitus position, similar hyperechoic structures become visible in the right lobe of liver. What additional medical history would explain these findings?
Autosomal dominant polycystic kidney disease
ERCP and sphincterotomy
Previous Pneumocystis jiroveci (carinii) infection
Right hemicolectomy for colorectal cancer
Wilson’s disease
ANSWER: B
The ultrasound findings are typical of pneumobilia. Other causes include an incompetent sphincter of Oddi (usually in elderly patients) and a surgical procedure involving a Roux loop.
Reference: Grainger & Allison’s 5e, pp 734-736.


QUESTION 77
A 48-year-old man has a strong family history of colorectal cancer. He is found to have a mild microcytic anaemia and a stool sample for faecal occult blood testing is positive. A CT colonography is performed and, on 3D images, a 1-cm focal polypoid mass is seen in the wall of the sigmoid colon. The reporting radiologist is unsure whether this lesion is significant and reviews the 2D supine and prone axial images. Which additional feature would be most consistent with a polyp?
The lesion contains a locule of gas at its base.
The lesion has a mean density of — 150 HU.
The lesion is of homogeneous attenuation.
The lesion lies on the dependent surface of the bowel on prone and supine images.
There are diverticulae seen in the sigmoid colon.
ANSWER: C
A polyp will usually demonstrate uniform soft tissue density, similar to the surrounding bowel wall.
Reference: Grainger & Allison’s 5e, pp 685–686.


QUESTION 78
A 23-year-old man presents with a 2-day history of vomiting and generalised abdominal pain. Two years ago, he underwent a small bowel resection for an ileal stricture due to Crohn’s disease. Initial blood tests reveal a raised CRP and white cell count and an abdominal radiograph demonstrates dilated loops of small bowel. Small bowel obstruction is suspected and a contrast-enhanced CT of the abdomen is performed. Which one of the following statements is true regarding the role of multidetector CT in small bowel obstruction?
Five to 15% of small bowel obstructions are due to hernias.
Twenty to 30% of small bowel obstructions are due to adhesions.
Bowel wall thickening and intramural gas indicate the presence of pneumatosis coli.
Closed loop obstruction is less likely to result in bowel ischaemia than simple obstruction.
In small bowel obstruction due to adhesions, a transition point will not be seen.
ANSWER: A
Bowel wall thickening, lack of enhancement, adjacent fluid, and pneumatosis intestinalis are all CT signs of ischemia (strangulation) in small bowel obstruction. Fifty to 80% of small bowel obstruction is attributable to adhesions, while 10% is due to hernias. In adhesions, there is usually a history of previous abdominal surgery with CT demonstrating small bowel obstruction. The transition point may be identified, but the actual adhesive band is usually not visualized.
Reference: Qalbani A, Paushter D, Dachman AH. Multidetector row CT of small bowel obstruction. Radiol Clin North Am 2003; 45(3):499-512.


QUESTION 79
A 27-year-old woman is admitted to hospital with an episode of mild acute pancreatitis. An abdominal ultrasound demonstrates no gallstones or biliary dilatation and the pancreas appears normal. She is managed conservatively and discharged after 7 days. Three months later, she is seen in the outpatient clinic and complains of worsening upper abdominal pain. A contrast-enhanced CT demonstrates a 6-cm cystic mass in the pancreatic body with a thin enhancing wall. Which statement is true regarding this cystic pancreatic mass?
Forty to 60% will resolve spontaneously.
Eighty to 90% occur within 7 days of acute pancreatitis.
Gas within the lesion would be pathognomonic of an enteric fistula.
Surgical drainage will be required to confirm the diagnosis.
The cyst fluid is likely to have low amylase content.
ANSWER: A
The majority of symptomatic pancreatic cysts are pseudocysts; approximately half of pancreatic pseudocysts resolve spontaneously.
Reference: Grainger & Allison’s 5e, pp 796-797, 808.


QUESTION 80
A 67-year-old woman undergoes surgical resection of a distal sigmoid adenocarcinoma. The surgeon performs a primary anastomosis between the descending colon and rectum and leaves a defunctioning loop colostomy. Nine days later, the patient is experiencing fevers and low abdominal pain. A contrast-enhanced CT shows a small fluid collection around the anastomosis with no definite abscess identified. The surgical team are concerned about the integrity of the anastomosis. Which investigation would you choose to look for an anastomotic leak?
Barium enema
Barium follow-through
MRI pelvis with intravenous gadolinium
Water-soluble contrast cystogram
Water-soluble contrast enema
ANSWER: E
The combination of water-soluble contrast enema and CT is used to look for anastomotic leakage and abscess formation.
Reference: Grainger & Allison’s 5e, p 702.


QUESTION 81
A 64-year-old woman presents to her GP with increasing discomfort in her upper abdomen and anorexia. There is a past medical history of gallstones. The GP requests an abdominal ultrasound and this demonstrates a 6 x 4 cm mixed echogenicity lesion in the gallbladder fossa, with the gallbladder not separately visualised. On CT, the gallbladder fossa mass demonstrates central low attenuation with peripheral enhancement and mild intrahepatic biliary dilatation. Low attenuation lymph nodes are present at the porta hepatis (measuring up to 1.5 cm short axis). Which diagnosis is most likely?
Adenomyomatosis
Gallbladder carcinoma
Hepatocellular carcinoma
Porcelain gallbladder
Xanthogranulomatous cholecystitis
ANSWER: B
A gallbladder fossa mass with little or no visible normal gallbladder and hilar biliary obstruction is highly suggestive of gallbladder carcinoma.
References: Grainger & Allison’s 5e, p 772; Gore RM, Yaghmai V, Newmark GM, et al. Imaging benign and malignant disease of the gallbladder. Radiol Clin North Am 2002; 40:1307-1323.


QUESTION 82
A 52-year-old man is investigated for weight loss and dyspepsia. At endoscopy, an adenocarcinoma of the posterior wall of the gastric body is visualised and confirmed on histology. A contrast-enhanced CT of the abdomen is performed (with intravenous Buscopan and water as oral contrast) to stage the tumour. The primary tumour is seen as focal gastric mucosal thickening with a small amount of free fluid noted in the left paracolic gutter and pelvis. An endoscopic ultrasound is performed and shows that the tumour extends beyond the serosal surface of the posterior gastric wall. Which structure is most at risk of direct invasion by this tumour?
Abdominal aorta
Left lobe of liver
Pancreas
Right diaphragmatic crus
Transverse colon
ANSWER: C
The body and tail of the pancreas lie posterior to the stomach and can be infiltrated by direct extension of a gastric tumor.
Reference: Grainger & Allison’s 5e, pp 646-647.


QUESTION 83
A 22-year-old woman attends the Emergency Department with a 10-day history of vomiting and diarrhoea. The symptoms have worsened and are now associated with severe abdominal pain. Initial investigations reveal an elevated neutrophil count and CRP, and she is treated with intravenous fluids and antiemetics. In view of increased pain and fever, a contrast-enhanced CT of the abdomen and pelvis is performed and shows that a segment of bowel is significantly thickened. The microbiology laboratory telephones the clinical team and states that Yersinia enterocolitica has been isolated from the patient’s stool samples. Which segment of the bowel is likely to be abnormal?
Duodenum
Gastric antrum
Proximal jejunum
Sigmoid colon
Terminal ileum
ANSWER: E
An increased number of thickened valvulae conniventes are seen in the distal ileum with nodular filling defects due to lymphoid hyperplasia.
Reference: Grainger & Allison’s 5e, p 671.


QUESTION 84
A 74-year-old woman is referred to hospital by her GP as an emergency medical admission. The referral letter indicates that the patient is in residential care and has Alzheimer’s disease. Her carers have noticed generalised malaise and significant weight loss over the past 6 weeks. A contrast-enhanced CT is performed and demonstrates multiple low attenuation liver metastases. These lesions contain foci of amorphous calcification and show rim enhancement in the portal venous phase. What is the most likely underlying malignancy in this patient?
Carcinoid tumour of ileum
Endometrial carcinoma
Mucinous adenocarcinoma of colon
Multifocal hepatocellular carcinoma
Papillary carcinoma of thyroid
ANSWER: C
Calcification occurs in 2-3% of liver metastases. Mucinous adenocarcinoma of the GI tract is the most frequent underlying primary tumor.
Reference: Grainger & Allison’s 5e, pp 750-751.


QUESTION 85
A 79-year-old woman is admitted to hospital with a 2-day history of diarrhoea and abdominal pain. A contrast-enhanced CT of the abdomen demonstrates mucosal thickening of the proximal descending colon with a low attenuation ‘target sign’ appearance. The rectosigmoid and right hemicolon are normal in appearance. The patient is managed conservatively and the symptoms resolve. Six months later, a double contrast barium enema is performed and shows an irregular stricture of the descending colon with barium sacculation. What was the original diagnosis?
Acute diverticulitis
Giardiasis
Ischaemic colitis
Pseudomembranous colitis
Ulcerative colitis
ANSWER: C
Stricture formation (with barium sacculation on double contrast enema) can occur in the splenic flexure due to fibrosis of the ischemic bowel.
Reference: Grainger & Allison’s 5e, pp 697-698.


QUESTION 86
A 32-year-old man presents to his GP with increasing pain on swallowing solids and liquids. He has lost 15 kg in weight over the preceding 2 months. After a full history and examination, he is found to be HIV positive with a very low CD4 count. The GP refers him for a barium swallow examination and this demonstrates a single ulcer in the mid-oesophagus. The ulcer has a smooth margin, measures 4 cm in length and is oval in shape. There is no stricture identified. Which diagnosis is most likely?
Candida oesophagitis
CMV oesophagitis
Intramural pseudodiverticulosis
Oesophageal lymphoma
Squamous cell carcinoma of the oesophagus
ANSWER: B
A single ‘giant’ ulcer in an immunocompromised host is highly suggestive of viral esophagitis (e.g., CMV or herpes simplex).
Reference: Grainger & Allison’s 5e, pp 623-624.


QUESTION 87
A 46-year-old woman was diagnosed with breast cancer 3 months ago. A recent abdominal ultrasound identified a solitary liver lesion and an MRI of the liver is performed. This demonstrates a 2.5-cm diameter mass in liver segment 8. This lesion has a well-defined, lobulated contour and yields high T2 signal. An extended echo time of 180 ms is used and the lesion remains of high T2 signal (greater than the spleen, less than CSF). What is the most likely diagnosis?
Breast cancer metastasis
Focal nodular hyperplasia
Haemangioma
Hepatic adenoma
Simple liver cyst
ANSWER: C
Extended echo times will emphasize the high T2 signal intensity of liver hemangiomas, compared to surrounding structures.
Reference: Grainger & Allison’s 5e, pp 738-742.



QUESTION 88
A 49-year-old woman has experienced increasing difficulty swallowing over the past 6 months, with associated retrosternal discomfort. A barium swallow is performed and demonstrates virtually no peristaltic activity within a dilated oesophagus. The gastro-oesophageal junction appears widened and there is marked reflux of barium when the patient lies supine. An upper GI endoscopy shows moderate reflux oesophagitis. Given these findings, what is the most likely underlying diagnosis?
Achalasia
Oesophageal web
Presbyoesophagus
Scleroderma
Squamous cell carcinoma of oesophagus
ANSWER: D
The esophagus is the most commonly involved part of the GI system in scleroderma. Esophageal strictures can develop due to severe reflux.
References: Grainger & Allison’s 5e, p 623; Chapman & Nakielny, Aids to Radiological Differential Diagnosis, pp 131–132.


QUESTION 89
A 44-year-old man has liver cirrhosis due to chronic hepatitis B infection. He is admitted to hospital with decompensated liver disease and a serum alpha fetoprotein level is found to be markedly elevated. An abdominal ultrasound demonstrates a 3-cm hypoechoic mass in liver segment 5 with no colour flow demonstrated in an adjacent branch of the portal vein. The ultrasound probe is positioned over this focal lesion and an intravenous microbubble contrast agent is injected in the patient’s left arm. At what stage will this liver lesion appear most echogenic?
Pre contrast injection
15–30 seconds post injection
60–80 seconds post injection
5 minutes post injection
10 minutes post injection
ANSWER: B
Microbubble contrast agents act as positive contrast on ultrasound, and enhancement is seen as increasing echogenicity following contrast injection.
Reference: Grainger & Allison’s 5e, pp 75-76, 745-748.


QUESTION 90
A 41-year-old man has a 3-month history of weight loss and recurrent central abdominal pain. The pain is intermittent and radiates from the epigastrium through to his back. His past medical history includes excessive alcohol consumption and two previous admissions to hospital for acute pancreatitis. A contrast-enhanced CT of the abdomen is performed with precontrast, arterial and portal venous phase images of the upper abdomen. Which CT finding would be more suggestive of chronic pancreatitis than ductal pancreatic adenocarcinoma?
Common bile duct dilatation
Focal enlargement of the pancreatic head
Intraductal pancreatic calcification
Peripancreatic fat stranding and ascites
Reduced enhancement of body of pancreas
ANSWER: C
Intraductal calcification may be focal or diffuse and is not seen in all patients with chronic pancreatitis. However, when present, it is a highly reliable sign of chronic pancreatitis.
References: Grainger & Allison’s 5e, pp 799-800; Renter EM, Baker ME. Imaging of chronic pancreatitis. Radiol Clin North Am 2002; 45:1229-1242.


QUESTION 91
A 27-year-old woman presents to the Emergency Department with a 3-day history of sharp pain in the left iliac fossa. A transvaginal pelvic ultrasound is performed and shows a 5-cm unilocular cyst in the left ovary. The radiologist then performs a transabdominal ultrasound to assess the kidneys. It is noted that the liver parenchyma extends significantly below the right costal margin and passes anterior to the right kidney. The liver texture appears uniformly normal. What is the most likely explanation for the appearance of the liver?
Biliary hamartoma
Fitz-Hugh-Curtis syndrome
Focal fatty infiltration
Focal nodular hyperplasia (FNH)
Riedel’s lobe
ANSWER: E
Riedel’s lobe is described as a ‘tongue-like’ projection of the anterior tip of the right lobe of the liver. It is a variant of normal anatomy and is more common in women.
Reference: Grainger & Allison’s 5e, p 726.


QUESTION 92
A 56-year-old woman is found to have a 2.5-cm renal cell carcinoma in the upper pole of the right kidney. A contrast-enhanced CT of the chest and abdomen is performed and shows no evidence of local lymphadenopathy or distant metastases. The reporting radiologist notes a 2-cm cystic lesion in the pancreatic body. When assessing this cystic pancreatic lesion, which one of the following statements is true?
Eighty to 90% of symptomatic cystic lesions are pseudocysts.
Ninety to 95% of serous cystadenomas (microcystadenomas) contain calcification.
An asymptomatic solitary 8-mm simple cyst requires mandatory follow-up.
In a mucinous cystadenoma (macrocystadenoma), multiple small cysts typically measure up to 20 mm each.
The majority of mucinous cystadenomas occur in the pancreatic head.
ANSWER: A
The majority of symptomatic cystic pancreatic lesions are pseudocysts, and many will resolve spontaneously. Serous cystadenomas can occur anywhere in the pancreas and contain multiple small cysts measuring up to 20 mm each, while up to one-third may contain calcification. Ninety percent of mucinous (macrocystic) cystadenomas occur in the pancreatic body and tail, with cysts typically measuring greater than 20 mm. Long-term follow-up of cystic pancreatic lesions indicates that an asymptomatic simple cyst measuring less than 20 mm is unlikely to become clinically significant.
Reference: Planner AC, Anderson EM, Slater A, et al. An evidence-based review for the management of cystic pancreatic lesions. Clin Radiol 2007; 62:930-937.


QUESTION 93
A 64-year-old man sees his GP with a 2-month history of unexplained weight loss. He has experienced right upper quadrant discomfort and blood tests show an elevated bilirubin and gamma glutamyltransferase (GGT) with grossly elevated alkaline phosphatase. An abdominal ultrasound performed 6 months ago was normal with no evidence of gallstones. Which factor would not increase this patient’s risk of cholangiocarcinoma?
Caroli’s disease
Clonorchis sinensis infection
Exposure to iohexol 15 years ago
Primary sclerosing cholangitis
Type 1 choledochal cyst
ANSWER: C
Iohexol is a widely used low osmolar contrast medium and does not confer increased risk of biliary tract malignancy. Previous exposure to Thorotrast (thorium dioxide) is a recognized risk factor, however.
References: Grainger & Allison’s 5e, pp 781-782; Baron RL, Tublin ME, Peterson MS. Imaging the spectrum of biliary tract disease. Radiol Clin North Am 2002; 40:1325-1354.


QUESTION 94
A 71-year-old woman has a contrast-enhanced CT of the abdomen and pelvis to investigate lower abdominal pain and reduced bowel habit. An abnormal mesenteric soft tissue mass is present and displaces adjacent loops of bowel. The mass has multiple linear strands that radiate out towards the adjacent bowel loops giving a ‘stellate’ appearance. Which term describes this CT appearance?
Aneurysmal dilatation
Desmoplastic reaction
Omental cake
Peritoneal seeding
Sandwich encasement
ANSWER: B
The word desmoplastic comes from the Greek ‘desmos’ and ‘plasty’, meaning ‘to form a band’. It describes the growth of fibrous bands infiltrating adjacent tissue and is a recognized feature of GI carcinoid tumors.
Reference: Grainger & Allison’s 5e, pp 667-669, 721-722.


QUESTION 95
A 24-year-old man is referred to the gastroenterology outpatient clinic. He describes intermittent bloody diarrhoea with abdominal pain and has lost 5 kg in weight over the past 6 months. His father and uncle both have inflammatory bowel disease. Routine laboratory investigations are remarkable for a moderately elevated CRP. A double contrast barium enema examination is performed. Which of the following findings would be more consistent with Crohn’s disease than ulcerative colitis?
Aphthous ulceration interspersed with areas of normal mucosa
Fine granular appearance of the descending and sigmoid colon
Isolated involvement of the rectum and sigmoid
Shortening and narrowing of the entire colon with absence of haustral folds
The presence of ‘collar button’ ulceration
ANSWER: A
Aphthous ulceration is the earliest sign of Crohn’s disease on a double contrast barium enema. The other options are true for ulcerative colitis, ranging from the earliest signs of fine mucosal granularity to the ‘lead pipe’ appearance of the colon in chronic UC. Submucosal ulceration can extend laterally in UC, giving the ‘collar button’ appearance.
Reference: Ambrosini R, Barchiesi A, De Mizio D, et al. Inflammatory disease of the colon: how to image. Br J Radiol 2007; 61:442-448.


QUESTION 96
A 30-year-old man attends the Emergency Department with a 2-day history of abdominal pain and vomiting. On examination, he is afebrile with a firm mass palpable in the right lower quadrant of the abdomen. A supine abdominal radiograph is performed and demonstrates dilated loops of small bowel with a large soft tissue mass in the right lower quadrant. On ultrasound, the mass has a ‘pseudotumour’ appearance. What is the most likely diagnosis?
Colonic carcinoma
Gallstone ileus
Intussusception
Psoas abscess
Strangulated femoral hernia
ANSWER: C
The ‘pseudotumor’, ‘pseudokidney’, and ‘target’ signs all describe the characteristic sonographic appearance of intussusception.
Reference: Grainger & Allison’s 5e, pp 595, 1499-1501.


QUESTION 97
An 83-year-old man undergoes an emergency left hip hemiarthroplasty following a fractured neck of femur. Six days after surgery, he develops increasing abdominal distension with nausea and vomiting. An abdominal radiograph is performed and demonstrates dilatation of the ascending and transverse colon with the caecum measuring 7.0 cm in diameter. The clinical team believe that the patient may have colonic pseudo-obstruction and a single contrast (instant) enema is performed using water-soluble contrast. What are the likely findings in colonic pseudo-obstruction?
Extrinsic compression of the sigmoid colon
Long, irregular stricture of the sigmoid colon
Long, smooth stricture at the splenic flexure
No stricture demonstrated
Short ‘apple core’ stricture of the descending colon
ANSWER: D
An instant enema can exclude mechanical obstruction in patients with colonic pseudo-obstruction.
Reference: Grainger & Allison’s 5e, pp 598-599.


QUESTION 98
A 49-year-old man is involved in a road traffic accident and sustains serious head and chest injuries. He is ventilated on the intensive care unit and his injuries are managed conservatively. Ten days later, he develops a temperature of 39.5°, becomes tachycardic and requires inotropic support to maintain his blood pressure. An abdominal ultrasound is performed and shows a cystic structure in the right upper quadrant measuring 12 x 8 cm in size. The mass has a 6-mm thick wall, contains a layer of echogenic material and is surrounded by a rim of fluid. What is the most likely diagnosis?
Acalculous cholecystitis
Acute cholangitis
Gallbladder haematoma
Traumatic hepatic artery pseudoaneurysm
Xanthogranulomatous cholecystitis
ANSWER: A
Acalculous cholecystitis should always be considered in the seriously ill patient who develops unexplained sepsis.
Reference: Grainger & Allison’s 5e, pp 770-771.


QUESTION 99
A 59-year-old woman is found to have several small lesions within the liver on abdominal ultrasound. The ultrasound had been requested for investigation of abnormal liver function tests. An MRI of the liver demonstrates several low T2 signal lesions within the liver parenchyma. These lesions yield high signal on T1w images and, following intravenous gadolinium, there is avid enhancement in the hepatic arterial phase. Which diagnosis would best explain these findings?
Colorectal metastases
Focal fatty infiltration
Focal fatty sparing
Melanoma metastases
Multifocal HCC
ANSWER: D
Melanoma metastases have a different appearance from most liver metastases, as the paramagnetic effect of melanin leads to high T1 and low T2 signal.
References: Grainger & Allison’s 5e, pp 746-748, 751; Chapman & Nakielny, Aids to Radiological Differential Diagnosis, p 177.


QUESTION 100
A 72-year-old woman is brought to the Emergency Department with an 8-hour history of profuse fresh rectal bleeding. She had been awaiting endoscopic investigation of iron deficiency anaemia, but has no other significant medical history. On examination, she is haemodynamically unstable and blood tests reveal Hb = 5.0 g/dL. Following resuscitation, the patient’s condition stabilises and the surgical team request radiological investigation to identify the source of GI bleeding. Which statement is true regarding this clinical scenario?
Catheter angiography of the mesenteric vessels is the most sensitive method for detecting lower GI bleeding.
Colorectal cancer is the most common cause of profuse lower GI haemorrhage.
In fresh rectal bleeding, selective catheterisation of the coeliac axis is not required during catheter angiography.
Isotope studies with Tc-99 m-labelled red blood cells can detect bleeding rates as low as 0.1 ml/min.
The most common site of colonic angiodysplasia is the descending colon.
ANSWER: D
Red cell scintigraphy is the most sensitive method of detecting active GI bleeding (catheter angiography can only detect bleeding of 0.5 ml/min).
Reference: Grainger & Allison’s 5e, pp 578-580.
"""

def parse_mcqs(mcqs_text):
    """Parses the MCQs from a plain text string."""
    questions = []
    current_question = {}
    lines = mcqs_text.strip().split("\n")
    pattern_question = re.compile(r"QUESTION \d+", re.IGNORECASE)
    pattern_answer = re.compile(r"ANSWER: (\w)", re.IGNORECASE)

    for i, line in enumerate(lines):
        line = line.strip()
        if pattern_question.match(line):
            if current_question:
                questions.append(current_question)
            current_question = {"question": "", "options": [], "answer": "", "explanation": "", "reference": ""}
        elif line.startswith("ANSWER:"):
            match = pattern_answer.match(line)
            if match:
                current_question["answer"] = match.group(1)
            # The explanation is assumed to be in the next line
            if i + 1 < len(lines):
                current_question["explanation"] = lines[i + 1].strip()
        elif line.startswith("Reference:"):
            current_question["reference"] = line.replace("Reference:", "").strip()
        elif current_question and not current_question["answer"]:
            if not current_question["question"]:
                current_question["question"] = line
            else:
                current_question["options"].append(line)

    if current_question:
        questions.append(current_question)
    
    return questions

def quiz_app(questions):
    """Runs the quiz app."""
    st.title("MCQ Quiz Game")
    st.markdown("Test your knowledge with the MCQs!")

    # Initialize session state
    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0
        st.session_state.score = 0
        st.session_state.questions_order = random.sample(range(len(questions)), len(questions))  # Random order
        st.session_state.completed = False

    if st.session_state.current_question_index < len(questions):
        question_index = st.session_state.questions_order[st.session_state.current_question_index]
        question = questions[question_index]

        # Display score
        st.sidebar.subheader(f"Current Score: {st.session_state.score}/{st.session_state.current_question_index}")
        
        st.subheader(f"Question {st.session_state.current_question_index + 1}")
        st.write(question["question"])
        
        selected_option = st.radio("Select your answer:", question["options"], key=st.session_state.current_question_index)
        
        if st.button("Submit Answer"):
            correct_option = question["options"][ord(question["answer"]) - ord("A")]
            if selected_option == correct_option:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect. Correct answer: {correct_option}")
            
            # Show the explanation
            st.markdown(f"**Explanation:** {question.get('explanation', 'No explanation provided.')}")
            st.markdown(f"**Reference:** {question.get('reference', 'No reference provided.')}")
            
            # Enable "Next Question" button after submitting
            st.session_state.allow_next = True
        
        if st.session_state.get("allow_next", False):
            if st.button("Next Question"):
                st.session_state.current_question_index += 1
                st.session_state.allow_next = False

    if st.session_state.current_question_index == len(questions):
        st.session_state.completed = True

    if st.session_state.completed:
        st.balloons()
        st.subheader("Quiz Completed!")
        st.write(f"Your final score: {st.session_state.score} / {len(questions)}")
        st.button("Restart Quiz", on_click=reset_quiz)

def reset_quiz():
    """Resets the quiz."""
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.questions_order = random.sample(range(len(st.session_state.questions)), len(st.session_state.questions))
    st.session_state.completed = False
    st.session_state.allow_next = False

def main():
    st.title("MCQ Quiz Generator")
    st.markdown("Answer the questions to test your knowledge.")

    # Parse the MCQs from the embedded text
    questions = parse_mcqs(mcqs_text)

    if questions:
        quiz_app(questions)
    else:
        st.error("No valid questions found in the embedded text.")

if __name__ == "__main__":
    main()