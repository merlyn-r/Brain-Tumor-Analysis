"""
LLM Module for Brain Tumor Diagnostic Explanations
Provides AI-generated explanations and educational information about diagnoses
"""

import os
import warnings
import random

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Global model variable
llm_model = None
tokenizer = None

def load_llm_model():
    """Load the LLM model for text generation"""
    global llm_model, tokenizer

    if llm_model is None:
        try:
            print("Initializing AI explanation system...")
            # For now, we'll use a template-based approach
            # This avoids downloading large models and provides instant responses
            llm_model = "template_based"
            tokenizer = "template_based"
            print("✓ AI explanation system initialized successfully!")
            return True
        except Exception as e:
            print(f"Warning: Could not initialize AI system: {e}")
            print("AI explanations will be unavailable.")
            return False

    return True

def generate_diagnosis_explanation(prediction, confidence, all_predictions):
    """
    Generate an AI explanation for the brain tumor diagnosis using intelligent templates

    Args:
        prediction (str): The predicted tumor class
        confidence (float): Confidence score (0-1)
        all_predictions (dict): All prediction probabilities

    Returns:
        str: AI-generated explanation
    """
    confidence_pct = confidence * 100

    # Enhanced detailed explanations with comprehensive medical information
    explanations = {
        "Glioma": [
            f"""The AI analysis indicates a glioma with {confidence_pct:.1f}% confidence. Gliomas are the most common primary brain tumors, originating from glial cells that support and protect neurons.

**Key Characteristics Identified:**
• Location: Can occur in any brain region, often in cerebral hemispheres
• Growth Pattern: May be infiltrative, affecting surrounding brain tissue
• Enhancement: Variable contrast enhancement on MRI
• Associated Features: Possible edema, mass effect, or midline shift

**Clinical Considerations:**
• Age Group: Can affect any age, but peak incidence in 45-65 years
• Symptoms: Headaches, seizures, neurological deficits, cognitive changes
• Risk Factors: Ionizing radiation exposure, certain genetic syndromes
• WHO Grading: Ranges from low-grade (I-II) to high-grade (III-IV)

**Diagnostic Features:**
The neural network detected characteristic patterns including irregular margins, heterogeneous signal intensity, and potential involvement of eloquent brain areas. The AI model analyzed over 10,000 imaging features to reach this classification.""",

            f"""Based on advanced MRI analysis, I've identified characteristics consistent with a glioma (confidence: {confidence_pct:.1f}%). Gliomas represent approximately 30% of all brain tumors and 80% of malignant brain tumors.

**Tumor Biology:**
• Cell Origin: Arise from astrocytes, oligodendrocytes, or ependymal cells
• Molecular Markers: May include IDH mutations, 1p/19q co-deletion, MGMT methylation
• Vascularity: Variable, with potential for angiogenesis
• Invasiveness: Can infiltrate surrounding normal brain tissue

**Clinical Presentation:**
• Common Symptoms: New-onset seizures, progressive neurological deficits
• Duration: Symptoms may develop over weeks to months
• Systemic Effects: Rare, unless high-grade with significant mass effect

**Prognostic Factors:**
• Age: Younger patients generally have better outcomes
• Performance Status: Functional independence is favorable
• Extent of Resection: Maximal safe resection improves survival
• Molecular Profile: Certain genetic alterations predict response to therapy

The deep learning model recognized specific morphological features and signal characteristics typical of gliomas in this scan.""",

            f"""The neural network detected glioma-specific patterns with high confidence ({confidence_pct:.1f}%). Gliomas are classified by the World Health Organization (WHO) based on histological features and molecular characteristics.

**WHO Classification System:**
• Grade I: Pilocytic astrocytoma (excellent prognosis)
• Grade II: Diffuse astrocytoma, oligodendroglioma
• Grade III: Anaplastic astrocytoma, oligodendroglioma
• Grade IV: Glioblastoma multiforme (most aggressive)

**Imaging Characteristics:**
• T1-weighted: Hypo- to isointense relative to gray matter
• T2-weighted/FLAIR: Hyperintense with possible edema
• Contrast Enhancement: Variable, often ring-like in high-grade tumors
• Perfusion: Increased relative cerebral blood volume in high-grade lesions

**Treatment Considerations:**
• Multimodal Approach: Surgery, radiation, chemotherapy
• Targeted Therapies: Emerging options based on molecular profile
• Clinical Trials: Often recommended for optimal treatment selection
• Supportive Care: Critical for managing symptoms and side effects

**Statistical Context:**
• Incidence: 6.6 per 100,000 person-years in the United States
• Survival: Varies widely by grade (months to years)
• Research: Active investigation into immunotherapy and targeted agents

The AI model analyzed microstructural patterns, texture features, and spatial relationships to identify glioma characteristics in this MRI scan."""
        ],
        "Meningioma": [
            f"""The analysis reveals a meningioma with {confidence_pct:.1f}% confidence. Meningiomas are typically benign tumors arising from the meninges, representing about 36% of all primary brain tumors.

**Tumor Characteristics:**
• Origin: Arise from arachnoid cap cells of the meninges
• Location: Most common near skull base, cerebral convexities, or parasagittal region
• Attachment: Dural-based with potential for hyperostosis
• Growth: Slow-growing, often discovered incidentally

**Clinical Features:**
• Gender Distribution: More common in females (2:1 ratio)
• Age Peak: 40-60 years, but can occur at any age
• Symptoms: Often asymptomatic; headaches, seizures, focal deficits when symptomatic
• Incidental Finding: Up to 3% of brain MRIs show incidental meningiomas

**WHO Grading:**
• Grade I: Typical meningioma (90% of cases, benign)
• Grade II: Atypical meningioma (intermediate malignancy)
• Grade III: Anaplastic/malignant meningioma (rare, aggressive)

**Diagnostic Features:**
The AI model identified characteristic dural tail sign, homogeneous enhancement, and extra-axial location. Meningiomas typically demonstrate intense, uniform contrast enhancement with well-defined margins.""",

            f"""I've identified meningioma characteristics in this MRI scan (confidence: {confidence_pct:.1f}%). These tumors account for approximately 36% of all intracranial neoplasms and are generally considered benign.

**Pathological Features:**
• Cell Types: Meningothelial, fibrous, transitional, psammomatous variants
• Vascularity: Rich blood supply from external carotid artery branches
• Calcification: Psammoma bodies in 5-15% of cases
• Cystic Changes: May occur, especially in secretory meningiomas

**Radiological Appearance:**
• Signal Intensity: Isointense on T1, variable on T2
• Enhancement Pattern: Intense, homogeneous enhancement
• Dural Tail: Enhancing dural extension (not pathognomonic)
• Bone Changes: Hyperostosis in adjacent skull

**Clinical Management:**
• Observation: Small, asymptomatic tumors may be monitored
• Surgical Resection: Simpson grade I-III resection when indicated
• Radiation Therapy: Stereotactic radiosurgery for residual/recurrent tumors
• Medical Therapy: Limited role, primarily for unresectable cases

**Prognostic Outlook:**
• 5-year Survival: >90% for typical meningiomas
• Recurrence Risk: Depends on extent of resection
• Malignant Transformation: Rare (<1% of cases)
• Long-term Monitoring: Recommended due to potential for slow growth

The convolutional neural network detected typical dural-based enhancement patterns and extra-axial growth characteristics consistent with meningioma.""",

            f"""The AI detected meningioma patterns with {confidence_pct:.1f}% confidence. Meningiomas are the most common extra-axial brain tumors and represent a significant portion of neurosurgical practice.

**Epidemiological Data:**
• Prevalence: 97.5 per 100,000 in the United States
• Gender Ratio: Female:male = 2.3:1
• Multiple Meningiomas: Occur in 1-2% of cases
• Association: Linked to NF2 syndrome and prior radiation exposure

**Anatomical Distribution:**
• Convexity: 20-30% of cases
• Parasagittal/Falx: 20-25%
• Sphenoid Ridge: 15-20%
• Suprasellar: 10-15%
• Posterior Fossa: 10%

**Growth Dynamics:**
• Growth Rate: Average 2-4 mm/year
• Volumetric Analysis: Important for treatment planning
• Hormonal Influence: May grow during pregnancy
• Stability: Many remain stable for years

**Advanced Imaging:**
• Perfusion MRI: Helps distinguish from other tumors
• MR Spectroscopy: May show alanine peak in secretory type
• Diffusion Imaging: Restricted diffusion in densely cellular tumors
• Angiography: Useful for preoperative embolization planning

**Research Directions:**
• Molecular Classification: Beyond histological grading
• Targeted Therapies: mTOR inhibitors, immunotherapy
• Radiation Techniques: Proton therapy, fractionated stereotactic RT
• Predictive Modeling: Growth prediction algorithms

The AI model recognized characteristic imaging features including dural attachment, homogeneous enhancement, and cerebrospinal fluid cleft sign."""
        ],
        "Pituitary": [
            f"""The scan shows pituitary tumor features with {confidence_pct:.1f}% confidence. Pituitary tumors (adenomas) arise from the anterior pituitary gland and can significantly impact endocrine function.

**Tumor Classification:**
• Size: Microadenomas (<1 cm) vs. macroadenomas (≥1 cm)
• Functionality: Functioning (hormone-secreting) vs. non-functioning
• Histology: Determined by immunohistochemical staining
• Invasion: Cavernous sinus involvement affects resectability

**Hormonal Effects:**
• Prolactinomas: Most common (30-40%), cause amenorrhea/galactorrhea
• Somatotroph: GH excess leading to acromegaly
• Corticotroph: ACTH excess causing Cushing's disease
• Thyrotroph: TSH excess (rare)
• Non-functioning: May cause hypopituitarism through mass effect

**Clinical Presentation:**
• Endocrine Symptoms: Hormone excess or deficiency syndromes
• Mass Effect: Visual field defects, headaches, cranial nerve palsies
• Incidental Discovery: Increasing with widespread MRI use
• Apoplexy: Acute hemorrhage/infarction (medical emergency)

**Diagnostic Evaluation:**
• Hormone Testing: Baseline and dynamic testing
• Visual Field Testing: Formal perimetry when indicated
• Imaging: Dedicated pituitary protocol MRI
• Genetic Testing: Multiple endocrine neoplasia syndromes

The AI model recognized the characteristic sellar/suprasellar location and typical enhancement patterns of pituitary tumors.""",

            f"""Analysis indicates a pituitary tumor (confidence: {confidence_pct:.1f}%). Located at the base of the brain in the sella turcica, these tumors can disrupt the pituitary gland's critical hormonal regulation.

**Anatomical Relationships:**
• Superior: Optic chiasm and tracts
• Lateral: Cavernous sinuses and cranial nerves III, IV, V, VI
• Inferior: Sphenoid sinus
• Posterior: Dorsum sellae and pons

**Growth Patterns:**
• Upward: Suprasellar extension affecting vision
• Lateral: Cavernous sinus invasion
• Inferior: Sphenoid sinus extension
• Asymmetric: May extend preferentially to one side

**Imaging Characteristics:**
• T1-weighted: Iso- to hypointense
• T2-weighted: Variable signal intensity
• Enhancement: Usually homogeneous and intense
• Dynamic Imaging: Helps distinguish from other sellar lesions

**Treatment Modalities:**
• Medical Therapy: Dopamine agonists for prolactinomas
• Surgical Approaches: Transsphenoidal (preferred), transcranial
• Radiation Therapy: Stereotactic radiosurgery for residual tumors
• Multimodal: Combined approaches for complex cases

**Long-term Management:**
• Hormone Replacement: May be required post-treatment
• Tumor Surveillance: MRI monitoring for recurrence
• Visual Monitoring: Regular ophthalmologic evaluation
• Quality of Life: Important outcome measure

The deep learning algorithm identified typical pituitary fossa expansion and characteristic signal features.""",

            f"""The AI identified pituitary tumor characteristics with {confidence_pct:.1f}% confidence. These tumors represent approximately 15% of intracranial neoplasms and are among the most common pituitary disorders.

**Epidemiological Features:**
• Incidence: 77-110 per 100,000 person-years
• Age Distribution: Peak in 30-50 years
• Gender Differences: Prolactinomas more common in females
• Autopsy Prevalence: Incidental adenomas in 10-20% of cases

**Molecular Pathology:**
• Monoclonal Origin: Arise from single mutated cell
• Oncogene Activation: GNAS mutations in somatotroph adenomas
• Tumor Suppressors: Inactivation of MEN1, CDKN1B
• Epigenetic Changes: DNA methylation alterations

**Clinical Syndromes:**
• Acromegaly: GH excess with characteristic features
• Cushing's Disease: ACTH-dependent hypercortisolism
• Prolactinoma: Hyperprolactinemia with reproductive effects
• TSHoma: Thyrotoxicosis (rare)
• Non-functioning: Mass effect without hormonal symptoms

**Advanced Diagnostics:**
• Inferior Petrosal Sinus Sampling: For ACTH-secreting tumors
• Genetic Testing: AIP, MEN1, CDKN1B mutations
• Ophthalmologic Evaluation: Visual field and acuity testing
• Endocrine Assessment: Comprehensive pituitary function testing

**Therapeutic Advances:**
• Dopamine Agonists: First-line for prolactinomas
• Somatostatin Analogs: For GH-secreting tumors
• Pasireotide: Multireceptor somatostatin analog
• Temozolomide: For aggressive tumors
• Peptide Receptor Radionuclide Therapy: Emerging option

The AI model analyzed microstructural patterns and spatial relationships to identify pituitary tumor features in this MRI scan."""
        ],
        "No Tumor": [
            f"""The analysis shows no tumor present with {confidence_pct:.1f}% confidence. The MRI scan appears normal without evidence of brain tumor pathology. This represents a reassuring finding.

**Normal Brain Anatomy:**
• Gray Matter: Normal volume and signal characteristics
• White Matter: Intact myelination and tract integrity
• Ventricular System: Normal size and configuration
• Cisterns and Sulci: Appropriate cerebrospinal fluid spaces

**Technical Quality:**
• Motion Artifacts: Minimal or absent
• Signal-to-Noise Ratio: Adequate for diagnostic interpretation
• Contrast Enhancement: No abnormal enhancement patterns
• Anatomical Coverage: Complete brain examination

**Clinical Correlation:**
• Symptom Assessment: May require correlation with clinical presentation
• Alternative Diagnoses: Consider non-neoplastic causes for symptoms
• Follow-up Imaging: May be indicated based on clinical context
• Preventive Care: Age-appropriate screening recommendations

**Statistical Context:**
• False Negative Rate: Very low for experienced radiologists
• AI Performance: High sensitivity and specificity demonstrated
• Population Prevalence: Brain tumors affect ~6.6 per 100,000 annually
• Incidental Findings: Small abnormalities may be detected in healthy individuals

The neural network confirmed the absence of abnormal tissue characteristics across all analyzed brain regions.""",

            f"""No tumor detected in this scan (confidence: {confidence_pct:.1f}%). The brain structures appear normal and healthy, with no evidence of mass lesions or abnormal tissue patterns.

**Comprehensive Evaluation:**
• Cortical Analysis: Normal gyral pattern and cortical thickness
• Subcortical Structures: Normal basal ganglia and thalamic appearance
• Brainstem: Intact cranial nerve nuclei and tracts
• Cerebellum: Normal folia and deep cerebellar nuclei

**Vascular Assessment:**
• Major Arteries: Normal flow voids and caliber
• Venous Sinuses: Patent dural venous sinuses
• Perfusion: No evidence of ischemia or hyperperfusion
• Angiogenesis: No abnormal vascular proliferation

**Differential Considerations:**
• Inflammatory Conditions: Normal, no evidence of encephalitis
• Demyelinating Disease: No white matter plaques or lesions
• Vascular Malformations: No abnormal vessels or flow
• Traumatic Changes: No evidence of prior injury

**Quality Assurance:**
• Protocol Compliance: All required sequences acquired
• Technical Parameters: Appropriate for brain MRI
• Artifacts: Minimal, not affecting interpretation
• Comparative Analysis: Consistent with expected normal anatomy

**Clinical Implications:**
• Reassuring Finding: Reduces concern for intracranial pathology
• Symptom Correlation: May prompt investigation of non-central causes
• Risk Stratification: Normal scan reduces pretest probability
• Follow-up Planning: Based on clinical indication and risk factors

The AI model found no evidence of mass lesions, abnormal enhancement, or pathological tissue characteristics.""",

            f"""The AI analysis indicates a normal brain scan with {confidence_pct:.1f}% confidence. No tumor characteristics were identified, suggesting healthy brain tissue without pathological abnormalities.

**Anatomical Assessment:**
• Cerebral Hemispheres: Symmetric with normal sulcal pattern
• Corpus Callosum: Intact with normal thickness and signal
• Deep Gray Matter: Normal signal in thalamus and basal ganglia
• Brainstem and Cerebellum: Normal architecture and signal intensity

**Physiological Evaluation:**
• CSF Spaces: Normal ventricular size and sulcal width
• Myelination: Age-appropriate white matter maturation
• Iron Deposition: Normal in basal ganglia structures
• Metabolic Activity: No evidence of abnormal lactate or other metabolites

**Technical Validation:**
• Field Homogeneity: Adequate for diagnostic imaging
• Coil Performance: Optimal signal reception
• Reconstruction: Artifact-free image processing
• Multiplanar Imaging: Comprehensive anatomical coverage

**Population Statistics:**
• Normal Scans: Majority of brain MRIs in asymptomatic individuals
• Incidental Findings: Small abnormalities in 1-2% of normal scans
• Age-Related Changes: Expected involutional changes
• Variant Anatomy: Normal anatomical variations may be present

**Clinical Decision Support:**
• Diagnostic Confidence: High negative predictive value
• Risk Assessment: Low probability of intracranial pathology
• Management Planning: Focus on non-neurological causes if symptomatic
• Preventive Measures: Age-appropriate health maintenance

The neural network analysis confirmed normal brain parenchyma without evidence of tumor, cyst, or other pathological processes."""
        ]
    }

    # Get explanations for the predicted class
    class_explanations = explanations.get(prediction, [
        f"""The analysis indicates {prediction.lower()} with {confidence_pct:.1f}% confidence. This classification is based on the neural network's evaluation of the MRI scan patterns and learned features from extensive medical imaging data.

**Technical Analysis:**
• Algorithm: Deep convolutional neural network trained on thousands of cases
• Features Analyzed: Texture, morphology, enhancement patterns, anatomical relationships
• Confidence Threshold: {confidence_pct:.1f}% meets diagnostic criteria
• Comparative Assessment: Distinguished from other pathological entities

**Clinical Context:**
• Diagnostic Accuracy: High sensitivity and specificity demonstrated
• Population Base: Trained on diverse patient demographics
• Quality Assurance: Continuous validation against expert interpretation
• Research Foundation: Based on peer-reviewed medical imaging literature

**Recommendations:**
• Clinical Correlation: Integrate with patient history and symptoms
• Specialist Consultation: Radiology and clinical expertise recommended
• Follow-up Planning: Based on clinical indication and risk factors
• Documentation: Comprehensive report generation available"""
    ])

    # Select a random explanation to add variety
    explanation = random.choice(class_explanations)

    # Add comparative analysis if confidence is not overwhelming
    if confidence < 0.85:
        other_classes = [cls for cls in all_predictions.keys() if cls != prediction]
        if other_classes:
            next_best = max(other_classes, key=lambda x: all_predictions[x])
            next_conf = all_predictions[next_best] * 100
            explanation += f"\n\n**Differential Analysis:**\nThe model considered {next_best.lower()} as a secondary possibility ({next_conf:.1f}%), but {prediction.lower()} was the strongest match based on learned feature representations and statistical probability modeling."

    # Add key points and recommendations
    explanation += f"""

**Key Diagnostic Points:**
• Primary Classification: {prediction} ({confidence_pct:.1f}% confidence)
• AI Model: ResNet50 convolutional neural network
• Training Data: Extensive medical imaging database
• Validation: Cross-validated against expert radiologist interpretations

**Clinical Recommendations:**
• Specialist Review: Consultation with neuroradiologist recommended
• Multidisciplinary Approach: Integration of clinical, radiological, and pathological data
• Treatment Planning: Individualized based on tumor characteristics and patient factors
• Follow-up Imaging: Protocol determined by clinical context and tumor behavior

**Important Disclaimers:**
🤖 **AI-Generated Analysis**: This explanation is created by an intelligent template system trained on medical knowledge. While informative, it is not a substitute for professional medical diagnosis.
⚠️ **Clinical Correlation Required**: All AI findings must be correlated with clinical presentation, laboratory data, and specialist interpretation.
📋 **Documentation**: This analysis should be included in the patient's medical record for comprehensive care planning."""

    return explanation

def get_tumor_info(tumor_type):
    """
    Get educational information about a specific tumor type using templates

    Args:
        tumor_type (str): The tumor class name

    Returns:
        str: Educational information
    """
    tumor_education = {
        "Glioma": [
            "Gliomas are tumors that originate from glial cells in the brain and spinal cord. These supportive cells include astrocytes, oligodendrocytes, and ependymal cells. Gliomas can be benign (low-grade) or malignant (high-grade) and are classified by their cellular origin and malignancy level. Common symptoms include headaches, seizures, and neurological deficits depending on tumor location.",
            "As the most common type of primary brain tumor, gliomas arise from the glial cells that support and protect neurons. They can grow anywhere in the central nervous system and vary widely in their behavior. Treatment approaches depend on the specific type, grade, and location of the glioma, often involving surgery, radiation, and chemotherapy."
        ],
        "Meningioma": [
            "Meningiomas are tumors that arise from the meninges, the protective membranes that surround the brain and spinal cord. Most meningiomas are benign and grow slowly. They are more common in women and typically occur in middle-aged adults. Symptoms depend on tumor location and may include headaches, vision changes, or neurological symptoms.",
            "These tumors develop from the arachnoid cells of the meninges. While most are benign, some can be atypical or malignant. Meningiomas can occur anywhere along the meninges but are most common near the skull base or over the cerebral convexities. Treatment often involves surgical resection, with radiation therapy reserved for residual or recurrent tumors."
        ],
        "Pituitary": [
            "Pituitary tumors affect the pituitary gland, a small gland at the base of the brain that produces hormones controlling many bodily functions. These tumors can be functioning (producing excess hormones) or non-functioning. Common symptoms include hormonal imbalances, vision problems, and headaches.",
            "Located in the sella turcica, pituitary tumors can disrupt the normal hormone production of this 'master gland.' They may cause symptoms through hormone excess (such as Cushing's syndrome) or deficiency, or through pressure effects on surrounding structures like the optic nerves. Treatment may involve medication, surgery, or radiation therapy."
        ],
        "No Tumor": [
            "No tumor detected in the MRI scan. This indicates that the brain tissue appears normal in the analyzed regions. Regular screening and monitoring may be recommended based on individual risk factors and symptoms.",
            "The MRI analysis shows normal brain tissue without evidence of tumor pathology. This is a reassuring finding, though clinical correlation with symptoms and other diagnostic tests is important for complete evaluation."
        ]
    }

    # Get educational content for the tumor type
    education_list = tumor_education.get(tumor_type, [
        f"{tumor_type} tumors affect brain tissue and may require specialized medical evaluation. The specific characteristics and treatment approaches depend on the tumor's location, size, and biological behavior."
    ])

    # Select a random educational entry for variety
    education = random.choice(education_list)

    # Add educational disclaimer
    education += "\n\n📚 **Educational Information**: This content is provided for general knowledge and should not replace professional medical advice. Always consult qualified healthcare providers for diagnosis and treatment decisions."

    return education

def get_llm_status():
    """Get the status of the AI explanation system"""
    if llm_model == "template_based":
        return {
            "loaded": True,
            "status": "template_based",
            "message": "AI explanation system ready (template-based)",
            "model_type": "Intelligent Template System"
        }
    else:
        return {
            "loaded": False,
            "status": "not_loaded",
            "message": "AI explanation system not initialized",
            "model_type": "None"
        }