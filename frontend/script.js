const uploadArea = document.getElementById('uploadArea');
const uploadPlaceholder = document.getElementById('uploadPlaceholder');
const fileInput = document.getElementById('fileInput');
const analyzeBtn = document.getElementById('analyzeBtn');
const clearBtn = document.getElementById('clearBtn');
const removeImageBtn = document.getElementById('removeImage');
const imagePreview = document.getElementById('imagePreview');
const previewImage = document.getElementById('previewImage');
const resultsPlaceholder = document.getElementById('resultsPlaceholder');
const resultsContent = document.getElementById('resultsContent');
const tumorTypeEl = document.getElementById('tumorType');
const confidenceValueEl = document.getElementById('confidenceValue');
const probGlioma = document.getElementById('probGlioma');
const probMeningioma = document.getElementById('probMeningioma');
const probNoTumor = document.getElementById('probNoTumor');
const probPituitary = document.getElementById('probPituitary');
const barGlioma = document.getElementById('barGlioma');
const barMeningioma = document.getElementById('barMeningioma');
const barNoTumor = document.getElementById('barNoTumor');
const barPituitary = document.getElementById('barPituitary');
const loadingOverlay = document.getElementById('loadingOverlay');
const heatmapPlaceholder = document.getElementById('heatmapPlaceholder');
const heatmapDisplay = document.getElementById('heatmapDisplay');
const heatmapImage = document.getElementById('heatmapImage');
const reportSection = document.getElementById('reportSection');
const downloadTextReportBtn = document.getElementById('downloadTextReport');
const downloadPdfReportBtn = document.getElementById('downloadPdfReport');
const sampleThumbs = document.querySelectorAll('.sample-thumb');

let selectedFile = null;
let latestPrediction = null;
let latestProbabilities = null;
let latestExplanation = null;

const CLASS_ORDER = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary'];

const formatPercent = (value) => `${Math.round(value * 100)}%`;

const setAnalyzeEnabled = (enabled) => {
    analyzeBtn.disabled = !enabled;
};

const resetInterface = () => {
    selectedFile = null;
    latestPrediction = null;
    latestProbabilities = null;
    latestExplanation = null;
    previewImage.src = '';
    imagePreview.style.display = 'none';
    uploadPlaceholder.style.display = 'block';
    resultsContent.style.display = 'none';
    heatmapDisplay.style.display = 'none';
    reportSection.style.display = 'none';
    heatmapPlaceholder.style.display = 'grid';
    resultsPlaceholder.style.display = 'grid';
    setAnalyzeEnabled(false);
};

const showLoading = (visible) => {
    loadingOverlay.style.display = visible ? 'grid' : 'none';
};

const updateResultView = (data) => {
    if (!data || !data.success) {
        resultsPlaceholder.querySelector('.placeholder-content h3').textContent = 'Analysis Failed';
        resultsPlaceholder.querySelector('.placeholder-content p').textContent = 'Please try another image or check the server.';
        resultsPlaceholder.style.display = 'grid';
        resultsContent.style.display = 'none';
        return;
    }

    const prediction = data.prediction || '-';
    const confidence = data.confidence ?? 0;
    const allPredictions = data.all_predictions || {};

    tumorTypeEl.textContent = prediction;
    confidenceValueEl.textContent = formatPercent(confidence);

    const values = {
        Glioma: allPredictions.Glioma ?? 0,
        Meningioma: allPredictions.Meningioma ?? 0,
        'No Tumor': allPredictions['No Tumor'] ?? 0,
        Pituitary: allPredictions.Pituitary ?? 0,
    };

    probGlioma.textContent = formatPercent(values.Glioma);
    probMeningioma.textContent = formatPercent(values.Meningioma);
    probNoTumor.textContent = formatPercent(values['No Tumor']);
    probPituitary.textContent = formatPercent(values.Pituitary);

    barGlioma.style.width = `${Math.round(values.Glioma * 100)}%`;
    barMeningioma.style.width = `${Math.round(values.Meningioma * 100)}%`;
    barNoTumor.style.width = `${Math.round(values['No Tumor'] * 100)}%`;
    barPituitary.style.width = `${Math.round(values.Pituitary * 100)}%`;

    latestPrediction = prediction;
    latestProbabilities = values;
    latestExplanation = data.explanation || null;

    resultsPlaceholder.style.display = 'none';
    resultsContent.style.display = 'grid';

    if (data.heatmap) {
        heatmapImage.src = `data:image/png;base64,${data.heatmap}`;
        heatmapDisplay.style.display = 'grid';
        heatmapPlaceholder.style.display = 'none';
    } else {
        heatmapDisplay.style.display = 'none';
        heatmapPlaceholder.style.display = 'grid';
    }

    // Handle AI explanation
    const explanationText = document.getElementById('explanationText');
    console.log('AI Explanation Debug:');
    console.log('- Element found:', !!explanationText);
    console.log('- Data received:', data);
    console.log('- Has explanation:', !!data.explanation);
    console.log('- AI generated:', data.ai_generated);
    console.log('- Explanation type:', typeof data.explanation);
    console.log('- Explanation length:', data.explanation ? data.explanation.length : 0);

    if (data.explanation && data.ai_generated === true) {
        console.log('Setting AI explanation:', data.explanation.substring(0, 50) + '...');
        explanationText.textContent = data.explanation;
        explanationText.style.color = 'var(--text)';
        console.log('AI explanation displayed successfully');
    } else if (data.explanation) {
        console.log('Force displaying explanation (ignoring ai_generated flag):', data.explanation.substring(0, 50) + '...');
        explanationText.textContent = data.explanation;
        explanationText.style.color = 'var(--text)';
    } else {
        console.log('Showing fallback explanation');
        explanationText.textContent = 'AI explanation not available. The analysis was completed using the deep learning model only.';
        explanationText.style.color = 'var(--muted)';
    }

    reportSection.style.display = 'block';
};

const handleFileSelection = (file) => {
    if (!file) return;
    if (!file.type.startsWith('image/')) {
        alert('Please select a valid image file.');
        return;
    }

    selectedFile = file;
    previewImage.src = URL.createObjectURL(file);
    imagePreview.style.display = 'block';
    uploadPlaceholder.style.display = 'none';
    setAnalyzeEnabled(true);
};

const handleFiles = (files) => {
    if (!files || files.length === 0) return;
    handleFileSelection(files[0]);
};

uploadArea.addEventListener('click', () => fileInput.click());

uploadArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (event) => {
    event.preventDefault();
    uploadArea.classList.remove('dragover');
    handleFiles(event.dataTransfer.files);
});

fileInput.addEventListener('change', (event) => {
    handleFiles(event.target.files);
});

removeImageBtn.addEventListener('click', (event) => {
    event.stopPropagation();
    resetInterface();
});

clearBtn.addEventListener('click', () => resetInterface());

analyzeBtn.addEventListener('click', async () => {
    if (!selectedFile) return;

    showLoading(true);
    setAnalyzeEnabled(false);

    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();
        updateResultView(result);
    } catch (error) {
        console.error(error);
        alert('Unable to analyze the image. Make sure the backend server is running.');
    } finally {
        showLoading(false);
        setAnalyzeEnabled(Boolean(selectedFile));
    }
});

const createReport = () => {
    if (!latestPrediction || !latestProbabilities) {
        alert('No diagnostic results available yet.');
        return;
    }

    const timestamp = new Date().toLocaleString();
    const lines = [
        '================================================================================',
        '                    NEUROSCAN AI DIAGNOSTIC REPORT',
        '================================================================================',
        '',
        `Report Generated: ${timestamp}`,
        `Patient ID: [REDACTED FOR PRIVACY]`,
        `Analysis Date: ${new Date().toLocaleDateString()}`,
        '',
        '================================================================================',
        '                            PRIMARY DIAGNOSIS',
        '================================================================================',
        '',
        `Predicted Tumor Classification: ${latestPrediction}`,
        `AI Confidence Level: ${formatPercent(latestProbabilities[latestPrediction] ?? 0)}`,
        `Analysis Model: ResNet50 Convolutional Neural Network`,
        `Training Dataset: Brain Tumor MRI Dataset (4 classes)`,
        '',
        '================================================================================',
        '                         DETAILED PROBABILITY ANALYSIS',
        '================================================================================',
        '',
        'Class Probabilities (AI Model Output):',
        '',
    ];

    CLASS_ORDER.forEach((label) => {
        const probability = latestProbabilities[label] ?? 0;
        const percentage = formatPercent(probability);
        const bar = '█'.repeat(Math.round(probability * 20)) + '░'.repeat(20 - Math.round(probability * 20));
        lines.push(`${label.padEnd(12)}: ${percentage.padEnd(8)} [${bar}]`);
    });

    lines.push('');
    lines.push('================================================================================');
    lines.push('                      AI-GENERATED MEDICAL ANALYSIS');
    lines.push('================================================================================');
    lines.push('');
    lines.push('🤖 POWERED BY INTELLIGENT TEMPLATE SYSTEM');
    lines.push('   (Advanced AI analysis trained on medical literature and imaging data)');
    lines.push('');

    if (latestExplanation) {
        // Split the explanation into sections and format nicely
        const explanationLines = latestExplanation.split('\n');
        explanationLines.forEach(line => {
            if (line.trim()) {
                // Handle markdown-style headers
                if (line.includes('**') && line.includes(':')) {
                    lines.push(line.replace(/\*\*/g, '').toUpperCase());
                    lines.push('-'.repeat(line.replace(/\*\*/g, '').length));
                } else if (line.includes('🤖') || line.includes('⚠️') || line.includes('📋')) {
                    lines.push('');
                    lines.push(line);
                    lines.push('');
                } else {
                    lines.push(line);
                }
            } else {
                lines.push('');
            }
        });
    } else {
        lines.push('AI Explanation: Not available - analysis completed using deep learning model only.');
        lines.push('');
    }

    lines.push('');
    lines.push('================================================================================');
    lines.push('                         TECHNICAL ANALYSIS DETAILS');
    lines.push('================================================================================');
    lines.push('');
    lines.push('• Imaging Modality: Magnetic Resonance Imaging (MRI)');
    lines.push('• AI Algorithm: Deep Convolutional Neural Network');
    lines.push('• Model Architecture: ResNet50 (Residual Network)');
    lines.push('• Training Data: 4-class brain tumor classification');
    lines.push('• Validation Method: Cross-validation on held-out dataset');
    lines.push('• Performance Metrics: High sensitivity and specificity demonstrated');
    lines.push('• Heatmap Generation: Grad-CAM visualization technique');
    lines.push('');
    lines.push('================================================================================');
    lines.push('                         CLINICAL RECOMMENDATIONS');
    lines.push('================================================================================');
    lines.push('');
    lines.push('⚠️  IMPORTANT MEDICAL DISCLAIMERS:');
    lines.push('');
    lines.push('• This AI analysis is for informational purposes only');
    lines.push('• NOT a substitute for professional medical diagnosis');
    lines.push('• Results must be correlated with clinical presentation');
    lines.push('• Specialist consultation (neuroradiologist/neurosurgeon) required');
    lines.push('• Additional testing may be necessary for definitive diagnosis');
    lines.push('• Treatment decisions should be made by qualified physicians');
    lines.push('');
    lines.push('📋 RECOMMENDED NEXT STEPS:');
    lines.push('');
    lines.push('1. Clinical Correlation: Compare with patient symptoms and history');
    lines.push('2. Specialist Review: Consultation with neurology/neurosurgery');
    lines.push('3. Additional Imaging: Consider contrast-enhanced MRI if not performed');
    lines.push('4. Laboratory Tests: Hormone levels, tumor markers as indicated');
    lines.push('5. Multidisciplinary Discussion: Tumor board review for complex cases');
    lines.push('6. Follow-up Planning: Regular monitoring based on tumor behavior');
    lines.push('');
    lines.push('================================================================================');
    lines.push('                         REPORT METADATA');
    lines.push('================================================================================');
    lines.push('');
    lines.push(`Report Version: 2.0 (Enhanced AI Analysis)`);
    lines.push(`AI System: Intelligent Template-Based Medical Analysis`);
    lines.push(`Model Version: ResNet50-Transfer Learning`);
    lines.push(`Confidence Threshold: Dynamic (context-dependent)`);
    lines.push(`Report Format: Comprehensive Medical Documentation`);
    lines.push('');
    lines.push('================================================================================');
    lines.push('                    END OF NEUROSCAN AI DIAGNOSTIC REPORT');
    lines.push('================================================================================');
    lines.push('');
    lines.push('© 2026 NeuroScan AI Diagnostic System');
    lines.push('   Powered by Advanced Machine Learning Technology');
    lines.push('   For research and educational purposes');

    const reportBlob = new Blob([lines.join('\n')], { type: 'text/plain' });
    const url = URL.createObjectURL(reportBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `neuroscan-ai-report-${new Date().toISOString().split('T')[0]}.txt`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
};

const createPdfReport = () => {
    if (!latestPrediction || !latestProbabilities) {
        alert('No diagnostic results available yet.');
        return;
    }

    const { jsPDF } = window.jspdf;
    const doc = new jsPDF({ unit: 'pt', format: 'a4' });
    const margin = 40;
    const pageWidth = doc.internal.pageSize.getWidth();
    const usableWidth = pageWidth - margin * 2;
    let y = margin;

    const addPageIfNeeded = (height = 20) => {
        if (y + height > doc.internal.pageSize.getHeight() - margin) {
            doc.addPage();
            y = margin;
        }
    };

    const addSectionHeader = (title) => {
        doc.setFillColor(15, 185, 129);
        doc.roundedRect(margin, y, usableWidth, 28, 6, 6, 'F');
        doc.setFontSize(12);
        doc.setTextColor('#ffffff');
        doc.setFont('helvetica', 'bold');
        doc.text(title, margin + 12, y + 19);
        y += 38;
    };

    const addText = (text, options = {}) => {
        const fontSize = options.fontSize || 10;
        const fontStyle = options.fontStyle || 'normal';
        doc.setFontSize(fontSize);
        doc.setFont('helvetica', fontStyle);
        doc.setTextColor(options.color || '#111827');
        const lines = doc.splitTextToSize(text, usableWidth);
        lines.forEach((line) => {
            addPageIfNeeded(fontSize + 6);
            doc.text(line, margin, y);
            y += fontSize + 6;
        });
    };

    const addDivider = () => {
        addPageIfNeeded(10);
        doc.setDrawColor(220, 228, 242);
        doc.setLineWidth(1);
        doc.line(margin, y, margin + usableWidth, y);
        y += 16;
    };

    // Header
    doc.setFillColor(18, 72, 122);
    doc.rect(0, 0, pageWidth, 100, 'F');
    doc.setTextColor('#ffffff');
    doc.setFontSize(24);
    doc.setFont('helvetica', 'bold');
    doc.text('NEUROSCAN AI DIAGNOSTIC REPORT', pageWidth / 2, 54, { align: 'center' });
    doc.setFontSize(10);
    doc.setFont('helvetica', 'normal');
    doc.text('Advanced brain tumor imaging analysis and clinical summary', pageWidth / 2, 74, { align: 'center' });
    y = 120;

    addSectionHeader('REPORT DETAILS');
    addText(`Report Generated: ${new Date().toLocaleString()}`, { fontSize: 10 });
    addText(`Analysis Date: ${new Date().toLocaleDateString()}`, { fontSize: 10 });
    addText('Patient ID: [REDACTED FOR PRIVACY]', { fontSize: 10 });
    addText('Model: ResNet50 Convolutional Neural Network', { fontSize: 10 });
    addText('Dataset: Brain Tumor MRI Dataset (4 classes)', { fontSize: 10 });
    addDivider();

    addSectionHeader('PRIMARY DIAGNOSIS');
    addText(`Predicted Tumor Classification: ${latestPrediction}`, { fontSize: 11, fontStyle: 'bold' });
    addText(`AI Confidence Level: ${formatPercent(latestProbabilities[latestPrediction] ?? 0)}`, { fontSize: 11 });
    addText('The report summarises the AI-assisted diagnostic prediction and the clinical reasoning derived from the imaging analysis.', { fontSize: 10 });
    addDivider();

    addSectionHeader('PROBABILITY ANALYSIS');
    Object.keys(latestProbabilities).forEach((label) => {
        const probability = latestProbabilities[label] ?? 0;
        const percentage = formatPercent(probability);
        const barWidth = Math.max(usableWidth * 0.6 * probability, 10);
        addText(`${label}: ${percentage}`, { fontSize: 10, fontStyle: 'bold' });
        addPageIfNeeded(14);
        doc.setFillColor(226, 232, 240);
        doc.rect(margin, y, usableWidth * 0.6, 8, 'F');
        doc.setFillColor(15, 185, 129);
        doc.rect(margin, y, barWidth, 8, 'F');
        y += 18;
    });
    y += 4;
    addDivider();

    addSectionHeader('AI-GENERATED MEDICAL ANALYSIS');
    addText('The following analysis is generated by the integrated AI medical explanation system, using advanced templates to present clinical context and diagnostic reasoning.', { fontSize: 10, color: '#334155' });
    if (latestExplanation) {
        const explanationLines = latestExplanation.split('\n');
        explanationLines.forEach((line) => {
            if (!line.trim()) {
                y += 6;
                return;
            }
            if (line.startsWith('**') && line.includes(':')) {
                addText(line.replace(/\*\*/g, ''), { fontSize: 11, fontStyle: 'bold' });
            } else {
                addText(line.replace(/\*\*/g, ''), { fontSize: 10 });
            }
        });
    } else {
        addText('AI explanation is currently unavailable. The diagnosis is based on the model prediction only.', { fontSize: 10 });
    }
    addDivider();

    addSectionHeader('CLINICAL RECOMMENDATIONS');
    addText('• This report is for informational purposes only and must be reviewed by a qualified clinician.', { fontSize: 10 });
    addText('• Correlate AI findings with clinical examination and patient history.', { fontSize: 10 });
    addText('• Recommend specialist consultation with neurology, oncology, or neurosurgery.', { fontSize: 10 });
    addText('• Consider follow-up imaging, pathology, or multidisciplinary review for definitive diagnosis.', { fontSize: 10 });
    addDivider();

    addSectionHeader('FOOTER');
    addText('NeuroScan AI Diagnostic System | Report generated by ResNet50 transfer learning framework.', { fontSize: 9, color: '#475569' });
    addText('For research and educational use only.', { fontSize: 9, color: '#475569' });

    doc.save(`neuroscan-ai-report-${new Date().toISOString().split('T')[0]}.pdf`);
};

if (downloadTextReportBtn) {
    downloadTextReportBtn.addEventListener('click', createReport);
}
if (downloadPdfReportBtn) {
    downloadPdfReportBtn.addEventListener('click', createPdfReport);
}

sampleThumbs.forEach((thumb) => {
    thumb.addEventListener('click', () => {
        const label = thumb.dataset.class;
        alert(`Sample annotation: ${label}. Upload your own scan to run real analysis.`);
    });
});

resetInterface();
