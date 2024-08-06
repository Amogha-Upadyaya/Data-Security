function showDropdown(regulation) {
    document.getElementById('info-text').style.display = 'none';
    document.getElementById('dropdown-container').style.display = 'block';
    document.getElementById('content-display').innerHTML = ''; // Clear previous content
    document.getElementById('topic-dropdown').selectedIndex = 0; // Reset dropdown

    // Customize the prompt text based on the regulation if needed
    document.getElementById('dropdown-container').innerHTML = `
        <label for="topic-dropdown">Choose a topic for ${regulation.toUpperCase()}:</label>
        <select id="topic-dropdown" onchange="showContent('${regulation}', this.value)">
            <option value="">Select...</option>
            <option value="scope">Scope</option>
            <option value="objective">Objective</option>
            <option value="rights-individuals">Rights of Individuals</option>
            <option value="rights-organizations">Rights of Organizations</option>
            <option value="consequences">Consequences</option>
        </select>
    `;
}

function showContent(regulation, topic) {
    let content = '';
    let header = '';
    switch (topic) {
        case 'scope':
            content = getScopeContent(regulation);
            header = 'Scope';
            break;
        case 'objective':
            content = getObjectiveContent(regulation);
            header = 'Objective';
            break;
        case 'rights-individuals':
            content = getRightsIndividualsContent(regulation);
            header = 'Rights of Individuals';
            break;
        case 'rights-organizations':
            content = getRightsOrganizationsContent(regulation);
            header = 'Rights of Organizations';
            break;
        case 'consequences':
            content = getConsequencesContent(regulation);
            header = 'Consequences';
            break;
        default:
            content = 'Select a topic from the dropdown';
            header = '';
            break;
    }
    document.getElementById('content-display').innerHTML = `<h2>${header}</h2><p>${content}</p>`;
    document.getElementById('dropdown-container').style.display = 'none';
    document.getElementById('info-text').style.display = 'none';
}

function getScopeContent(regulation) {
    switch (regulation) {
        case 'gdpr':
            return "General Data Protection Regulation (GDPR): Applies to all organizations operating within the European Union (EU) and to those outside the EU if they offer goods or services to, or monitor the behavior of, EU residents. It governs the collection, processing, and storage of personal data, providing individuals with rights such as data access, correction, and deletion.";
        case 'hipaa':
            return "Health Insurance Portability and Accountability Act (HIPAA): Applies to healthcare providers, health plans, and healthcare clearinghouses in the United States that handle protected health information (PHI). It mandates the safeguarding of PHI through administrative, physical, and technical safeguards.";
        case 'pdpa':
            return "Personal Data Protection Act (PDPA): Singaporean law that regulates the collection, use, and disclosure of personal data by organizations. It grants individuals rights over their data and imposes obligations on organizations to protect and manage personal data appropriately.";
        case 'lgpd':
            return "Brazilian General Data Protection Law (LGPD): Applies to any entity processing personal data in Brazil, regardless of where the entity is located. It provides data protection rights to individuals and imposes requirements on data controllers and processors, including obtaining consent and ensuring data security.";
        case 'ccpa':
            return "California Consumer Privacy Act (CCPA): Applies to for-profit businesses operating in California that meet certain thresholds (e.g., annual gross revenues over $25 million). It gives California residents rights regarding their personal data, such as the right to access, delete, and opt out of the sale of their data.";
        case 'pcidss':
            return "Payment Card Industry Data Security Standard (PCI DSS): Applies to any organization that handles payment card information, including merchants and service providers. It sets requirements for securing cardholder data through various controls, including encryption, access controls, and regular security testing.";
        case 'china-cyber-law':
            return "China's Cybersecurity Law: Applies to network operators and operators of critical information infrastructure in China. It focuses on ensuring cybersecurity, protecting personal information, and maintaining data security through regulations on data localization, network security, and incident reporting.";
        case 'iso27001':
            return "ISO/IEC 27001: A standard providing a framework for managing information security risks, including requirements for establishing, implementing, maintaining, and continually improving an information security management system (ISMS).";
        case 'nis-directive':
            return "Network and Information Systems (NIS) Directive: Applies to operators of essential services and digital service providers within the EU. It aims to enhance the overall cybersecurity posture by setting requirements for risk management, incident reporting, and cooperation among member states.";
        case 'fisma':
            return "Federal Information Security Management Act (FISMA): Applies to U.S. federal agencies, as well as contractors and organizations that handle federal information systems. It mandates the implementation of information security programs, including risk management and security controls, to protect federal information and systems.";
        default:
            return 'Select a regulation to view its scope.';
    }
}

function getObjectiveContent(regulation) {
    switch (regulation) {
        case 'gdpr':
            return "To enhance data protection and privacy for individuals within the European Union and the European Economic Area. It aims to give individuals more control over their personal data and to standardize data protection laws across Europe.";
        case 'hipaa':
            return "To protect the privacy and security of individuals' medical information and to ensure the confidentiality and integrity of health information transmitted electronically.";
        case 'pdpa':
            return "To govern the collection, use, and disclosure of personal data in Singapore, ensuring that individuals' personal data is handled responsibly and in compliance with privacy principles.";
        case 'lgpd':
            return "To regulate the processing of personal data in Brazil, ensuring privacy and protection of individuals' personal information and establishing guidelines for data collection, use, and sharing.";
        case 'ccpa':
            return "To provide California residents with greater transparency and control over their personal data, including the right to know what personal information is being collected, the right to request deletion, and the right to opt-out of data sharing.";
        case 'pcidss':
            return "To enhance the security of payment card transactions by establishing a set of standards designed to protect cardholder data and prevent data breaches in the payment card industry.";
        case 'china-cyber-law':
            return "To strengthen cybersecurity and protect personal information and critical information infrastructure in China. It aims to ensure the security and stability of the internet and information systems.";
        case 'iso27001':
            return "To provide a framework for establishing, implementing, maintaining, and continually improving an information security management system (ISMS) to protect sensitive information and manage security risks.";
        case 'nis-directive':
            return "To improve the cybersecurity of network and information systems across the European Union, focusing on essential services and digital service providers to enhance overall resilience and response to cyber incidents.";
        case 'fisma':
            return "To provide a comprehensive framework for ensuring the effectiveness of information security controls over federal information systems in the United States. It aims to protect the confidentiality, integrity, and availability of federal information systems.";
        default:
            return 'Select a regulation to view its objective.';
    }
}

function getRightsIndividualsContent(regulation) {
    switch (regulation) {
        case 'gdpr':
            return `
                <ul>
                    <li>Right to Access: Individuals can request access to their personal data held by organizations.</li>
                    <li>Right to Rectification: Individuals can request correction of inaccurate or incomplete data.</li>
                    <li>Right to Erasure (Right to be Forgotten): Individuals can request the deletion of their personal data under certain conditions.</li>
                    <li>Right to Restrict Processing: Individuals can request the restriction of processing their personal data.</li>
                    <li>Right to Data Portability: Individuals can request their data in a structured, commonly used format and transfer it to another organization.</li>
                    <li>Right to Object: Individuals can object to the processing of their personal data for certain purposes, including direct marketing.</li>
                    <li>Rights related to Automated Decision-Making: Individuals have the right to not be subject to decisions based solely on automated processing, including profiling, which has legal effects on them.</li>
                </ul>`;
        case 'hipaa':
            return `
                <ul>
                    <li>Right to Access: Individuals can access and obtain copies of their medical records.</li>
                    <li>Right to Correct Information: Individuals can request amendments to their medical records.</li>
                    <li>Right to Disclosure: Individuals can request a list of disclosures of their health information.</li>
                    <li>Right to Request Restrictions: Individuals can request restrictions on the use or disclosure of their health information.</li>
                    <li>Right to Confidential Communications: Individuals can request to receive communications in a specific way or location.</li>
                </ul>`;
        case 'pdpa':
            return `
                <ul>
                    <li>Right to Access: Individuals can access their personal data held by organizations.</li>
                    <li>Right to Correction: Individuals can request correction of inaccurate or incomplete personal data.</li>
                    <li>Right to Withdraw Consent: Individuals can withdraw consent for the collection, use, or disclosure of their personal data.</li>
                    <li>Right to Complain: Individuals can lodge complaints with the Personal Data Protection Commission (PDPC).</li>
                </ul>`;
        case 'lgpd':
            return `
                <ul>
                    <li>Right to Confirmation: Individuals can confirm the existence of processing activities involving their personal data.</li>
                    <li>Right to Access: Individuals can access their personal data held by organizations.</li>
                    <li>Right to Correction: Individuals can request the correction of inaccurate or incomplete personal data.</li>
                    <li>Right to Deletion: Individuals can request the deletion of their personal data under certain conditions.</li>
                    <li>Right to Data Portability: Individuals can request their data in a structured, commonly used format and transfer it to another organization.</li>
                    <li>Right to Information: Individuals can receive information about the entities with which their data has been shared.</li>
                    <li>Right to Withdraw Consent: Individuals can withdraw consent for the collection, use, or disclosure of their personal data.</li>
                    <li>Right to Object: Individuals can object to the processing of their personal data for certain purposes.</li>
                </ul>`;
        case 'ccpa':
            return `
                <ul>
                    <li>Right to Know: Individuals can request to know what personal data is being collected about them and how it is used.</li>
                    <li>Right to Delete: Individuals can request the deletion of their personal data held by organizations.</li>
                    <li>Right to Opt-Out: Individuals can opt-out of the sale of their personal data.</li>
                    <li>Right to Non-Discrimination: Individuals have the right not to be discriminated against for exercising their CCPA rights.</li>
                    <li>Right to Access: Individuals can request access to the specific pieces of personal data collected about them.</li>
                </ul>`;
        case 'pcidss':
            return `
                <ul>
                    <li>PCI DSS does not explicitly provide rights to individuals regarding their payment card data. It focuses on setting standards for organizations to protect cardholder data and maintain secure payment environments.</li>
                </ul>`;
        case 'china-cyber-law':
            return `
                <ul>
                    <li>Right to Access: Individuals can request access to their personal data held by network operators.</li>
                    <li>Right to Correction: Individuals can request correction of inaccurate or incomplete personal data.</li>
                    <li>Right to Deletion: Individuals can request the deletion of their personal data under certain conditions.</li>
                    <li>Right to Restrict Processing: Individuals can request the restriction of processing their personal data.</li>
                </ul>`;
        case 'iso27001':
            return `
                <ul>
                    <li>ISO/IEC 27001 is a standard for information security management systems (ISMS) and does not explicitly provide rights to individuals. It focuses on establishing, implementing, maintaining, and continually improving an ISMS to manage information security risks.</li>
                </ul>`;
        case 'nis-directive':
            return `
                <ul>
                    <li>The NIS Directive focuses on the security of network and information systems and does not explicitly provide rights to individuals. It aims to enhance the overall cybersecurity posture of essential services and digital service providers within the EU.</li>
                </ul>`;
        case 'fisma':
            return `
                <ul>
                    <li>FISMA focuses on the security of federal information systems and does not explicitly provide rights to individuals. It mandates federal agencies to implement information security programs to protect federal information and systems.</li>
                </ul>`;
        default:
            return 'Select a regulation to view the rights of individuals.';
    }
}

function getRightsOrganizationsContent(regulation) {
    switch (regulation) {
        case 'gdpr':
            return "Organizations must implement appropriate technical and organizational measures to ensure and demonstrate compliance with GDPR. They have the right to process personal data if they obtain proper consent, have a legal obligation, or have a legitimate interest.";
        case 'hipaa':
            return "Organizations must implement safeguards to protect PHI, conduct risk analyses, and comply with privacy and security rules. They have the right to use and disclose PHI for treatment, payment, and healthcare operations without individual authorization.";
        case 'pdpa':
            return "Organizations must obtain consent before collecting, using, or disclosing personal data, and must implement measures to protect data. They have the right to process personal data for purposes that individuals have been informed about and have consented to.";
        case 'lgpd':
            return "Organizations must ensure transparency, security, and accountability in data processing. They have the right to process personal data with the consent of the data subject or under other lawful bases provided by LGPD.";
        case 'ccpa':
            return "Organizations must provide transparency about data practices, allow consumers to opt-out of data selling, and comply with consumer requests regarding their data. They have the right to collect, use, and disclose personal data as long as they comply with CCPA requirements.";
        case 'pcidss':
            return "Organizations must comply with PCI DSS requirements to protect cardholder data. They have the right to process payment card transactions as long as they adhere to security standards.";
        case 'china-cyber-law':
            return "Organizations must implement security measures to protect network and information systems and personal data. They have the right to process personal data for legitimate business purposes and must comply with data localization requirements.";
        case 'iso27001':
            return "Organizations must establish, implement, maintain, and continually improve an ISMS to manage information security risks. They have the right to implement security controls to protect information assets.";
        case 'nis-directive':
            return "Organizations must take appropriate security measures and report significant incidents. They have the right to process data necessary to maintain the security and continuity of essential services and digital services.";
        case 'fisma':
            return "Federal agencies must implement information security programs to protect information systems. They have the right to process federal information and must comply with FISMA requirements.";
        default:
            return 'Select a regulation to view the rights of organizations.';
    }
}

function getConsequencesContent(regulation) {
    switch (regulation) {
        case 'gdpr':
            return `
                <ul>
                    <li>Fines: Organizations can face fines of up to €20 million or 4% of their annual global turnover, whichever is higher.</li>
                    <li>Reputational Damage: Non-compliance can lead to significant reputational damage, loss of customer trust, and potential loss of business.</li>
                    <li>Legal Actions: Individuals have the right to seek compensation for damages resulting from GDPR violations.</li>
                </ul>`;
        case 'hipaa':
            return `
                <ul>
                    <li>Fines: Civil penalties can range from $100 to $50,000 per violation, with an annual maximum of $1.5 million. Criminal penalties include fines and imprisonment for up to 10 years.</li>
                    <li>Reputational Damage: Breaches can lead to loss of patient trust and damage to the organization's reputation.</li>
                    <li>Legal Actions: Individuals affected by breaches may seek compensation for damages.</li>
                </ul>`;
        case 'pdpa':
            return `
                <ul>
                    <li>Fines: Organizations can face fines of up to SGD 1 million for breaches.</li>
                    <li>Reputational Damage: Non-compliance can result in reputational damage and loss of customer trust.</li>
                    <li>Legal Actions: Individuals can lodge complaints with the PDPC, which can lead to investigations and enforcement actions.</li>
                </ul>`;
        case 'lgpd':
            return `
                <ul>
                    <li>Fines: Organizations can face fines of up to 2% of their revenue in Brazil, limited to R$50 million per violation.</li>
                    <li>Reputational Damage: Non-compliance can lead to significant reputational damage and loss of customer trust.</li>
                    <li>Legal Actions: Individuals can seek compensation for damages resulting from LGPD violations.</li>
                </ul>`;
        case 'ccpa':
            return `
                <ul>
                    <li>Fines: Civil penalties can range from $2,500 per violation to $7,500 per intentional violation.</li>
                    <li>Reputational Damage: Non-compliance can lead to reputational damage and loss of consumer trust.</li>
                    <li>Legal Actions: Consumers have the right to sue for data breaches and seek statutory damages.</li>
                </ul>`;
        case 'pcidss':
            return `
                <ul>
                    <li>Fines: Payment brands may impose fines ranging from $5,000 to $100,000 per month for non-compliance.</li>
                    <li>Reputational Damage: Data breaches can lead to loss of customer trust and significant reputational damage.</li>
                    <li>Legal Actions: Organizations may face lawsuits from affected customers and partners.</li>
                </ul>`;
        case 'china-cyber-law':
            return `
                <ul>
                    <li>Fines: Organizations can face fines and other penalties for non-compliance with cybersecurity requirements.</li>
                    <li>Reputational Damage: Non-compliance can lead to reputational damage and loss of customer trust.</li>
                    <li>Legal Actions: Individuals affected by breaches can seek compensation for damages.</li>
                </ul>`;
        case 'iso27001':
            return `
                <ul>
                    <li>Fines: There are no direct fines for non-compliance with ISO/IEC 27001, but organizations may face contractual penalties or loss of business opportunities.</li>
                    <li>Reputational Damage: Non-compliance can lead to reputational damage and loss of customer trust.</li>
                    <li>Legal Actions: Organizations may face legal actions for failing to protect information assets as per contractual obligations.</li>
                </ul>`;
        case 'nis-directive':
            return `
                <ul>
                    <li>Fines: Organizations may face fines and penalties for non-compliance with NIS Directive requirements.</li>
                    <li>Reputational Damage: Non-compliance can lead to reputational damage and loss of customer trust.</li>
                    <li>Legal Actions: Organizations may face legal actions for failing to protect network and information systems.</li>
                </ul>`;
        case 'fisma':
            return `
                <ul>
                    <li>Fines: There are no direct fines for non-compliance with FISMA, but federal agencies may face budget cuts or other administrative penalties.</li>
                    <li>Reputational Damage: Non-compliance can lead to reputational damage and loss of public trust.</li>
                    <li>Legal Actions: Agencies may face legal actions for failing to protect federal information systems.</li>
                </ul>`;
        default:
            return 'Select a regulation to view the consequences of non-compliance.';
    }
}

function getComplianceStepsContent(regulation) {
    switch (regulation) {
        case 'gdpr':
            return `
                <ul>
                    <li>Data Mapping: Identify and document data flows and processing activities.</li>
                    <li>Data Protection Impact Assessment (DPIA): Conduct assessments for high-risk processing activities.</li>
                    <li>Privacy Notices: Update privacy policies to reflect GDPR requirements.</li>
                    <li>Consent Management: Obtain and manage explicit consent from individuals for data processing.</li>
                    <li>Data Subject Rights: Implement procedures to handle requests from individuals exercising their rights.</li>
                    <li>Data Breach Response: Establish and maintain data breach response plans.</li>
                    <li>Training and Awareness: Provide GDPR training for employees.</li>
                    <li>Data Protection Officer (DPO): Appoint a DPO if required by GDPR.</li>
                </ul>`;
        case 'hipaa':
            return `
                <ul>
                    <li>Risk Analysis: Conduct regular risk assessments to identify vulnerabilities and threats.</li>
                    <li>Policies and Procedures: Develop and implement HIPAA-compliant policies and procedures.</li>
                    <li>Training: Provide HIPAA training for employees.</li>
                    <li>Access Controls: Implement access controls to limit access to PHI.</li>
                    <li>Encryption: Encrypt PHI to protect it during storage and transmission.</li>
                    <li>Incident Response: Establish and maintain an incident response plan for data breaches.</li>
                    <li>Business Associate Agreements: Ensure agreements with business associates comply with HIPAA.</li>
                </ul>`;
        case 'pdpa':
            return `
                <ul>
                    <li>Data Inventory: Identify and document personal data held by the organization.</li>
                    <li>Consent Management: Obtain and manage consent for data processing activities.</li>
                    <li>Privacy Notices: Update privacy policies to reflect PDPA requirements.</li>
                    <li>Data Protection Officer (DPO): Appoint a DPO if required by PDPA.</li>
                    <li>Data Subject Rights: Implement procedures to handle requests from individuals exercising their rights.</li>
                    <li>Data Breach Response: Establish and maintain data breach response plans.</li>
                    <li>Training and Awareness: Provide PDPA training for employees.</li>
                </ul>`;
        case 'lgpd':
            return `
                <ul>
                    <li>Data Mapping: Identify and document data flows and processing activities.</li>
                    <li>Consent Management: Obtain and manage consent for data processing activities.</li>
                    <li>Privacy Notices: Update privacy policies to reflect LGPD requirements.</li>
                    <li>Data Protection Officer (DPO): Appoint a DPO if required by LGPD.</li>
                    <li>Data Subject Rights: Implement procedures to handle requests from individuals exercising their rights.</li>
                    <li>Data Breach Response: Establish and maintain data breach response plans.</li>
                    <li>Training and Awareness: Provide LGPD training for employees.</li>
                </ul>`;
        case 'ccpa':
            return `
                <ul>
                    <li>Data Inventory: Identify and document personal data held by the organization.</li>
                    <li>Privacy Notices: Update privacy policies to reflect CCPA requirements.</li>
                    <li>Consumer Requests: Implement procedures to handle requests from consumers exercising their CCPA rights.</li>
                    <li>Opt-Out Mechanism: Provide a mechanism for consumers to opt-out of the sale of their personal data.</li>
                    <li>Data Security: Implement security measures to protect personal data.</li>
                    <li>Training and Awareness: Provide CCPA training for employees.</li>
                </ul>`;
        case 'pcidss':
            return `
                <ul>
                    <li>Scope Definition: Identify the scope of the PCI DSS assessment.</li>
                    <li>Gap Analysis: Conduct a gap analysis to identify areas of non-compliance.</li>
                    <li>Remediation: Implement measures to address identified gaps.</li>
                    <li>Assessment: Perform a formal PCI DSS assessment with a Qualified Security Assessor (QSA).</li>
                    <li>Reporting: Prepare and submit the required PCI DSS compliance reports.</li>
                    <li>Maintenance: Continuously monitor and maintain PCI DSS compliance.</li>
                    <li>Training: Provide PCI DSS training for employees.</li>
                </ul>`;
        case 'china-cyber-law':
            return `
                <ul>
                    <li>Data Inventory: Identify and document personal data held by the organization.</li>
                    <li>Data Localization: Ensure personal data is stored within China as required.</li>
                    <li>Security Measures: Implement security measures to protect personal data and network systems.</li>
                    <li>Data Subject Rights: Implement procedures to handle requests from individuals exercising their rights.</li>
                    <li>Incident Response: Establish and maintain an incident response plan for data breaches.</li>
                    <li>Training and Awareness: Provide training on cybersecurity and data protection requirements.</li>
                </ul>`;
        case 'iso27001':
            return `
                <ul>
                    <li>ISMS Establishment: Establish an ISMS based on ISO/IEC 27001 requirements.</li>
                    <li>Risk Assessment: Conduct risk assessments to identify and evaluate information security risks.</li>
                    <li>Control Implementation: Implement security controls to mitigate identified risks.</li>
                    <li>Documentation: Document the ISMS policies, procedures, and controls.</li>
                    <li>Internal Audits: Conduct internal audits to assess the effectiveness of the ISMS.</li>
                    <li>Management Review: Perform regular management reviews of the ISMS.</li>
                    <li>Continuous Improvement: Continuously improve the ISMS based on audit findings and changing risks.</li>
                </ul>`;
        case 'nis-directive':
            return `
                <ul>
                    <li>Security Measures: Implement appropriate security measures to manage risks to network and information systems.</li>
                    <li>Incident Reporting: Establish procedures for reporting significant incidents to the relevant authorities.</li>
                    <li>Risk Management: Conduct risk assessments to identify and mitigate security risks.</li>
                    <li>Continuous Monitoring: Continuously monitor network and information systems for security threats.</li>
                    <li>Cooperation: Cooperate with national authorities and other relevant entities in handling cybersecurity incidents.</li>
                </ul>`;
        case 'fisma':
            return `
                <ul>
                    <li>Information Security Program: Establish and maintain an information security program for federal information systems.</li>
                    <li>Risk Management: Conduct risk assessments and implement measures to mitigate identified risks.</li>
                    <li>Security Controls: Implement security controls to protect federal information systems.</li>
                    <li>Continuous Monitoring: Continuously monitor information systems for security threats.</li>
                    <li>Incident Response: Establish and maintain an incident response plan for security incidents.</li>
                    <li>Compliance Reporting: Prepare and submit the required FISMA compliance reports.</li>
                </ul>`;
        default:
            return 'Select a regulation to view the steps to ensure compliance.';
    }
}

function updateContent(type, regulation) {
    let content = '';
    switch (type) {
        case 'rightsIndividuals':
            content = getRightsIndividualsContent(regulation);
            break;
        case 'rightsOrganizations':
            content = getRightsOrganizationsContent(regulation);
            break;
        case 'consequences':
            content = getConsequencesContent(regulation);
            break;
        case 'complianceSteps':
            content = getComplianceStepsContent(regulation);
            break;
        default:
            content = 'Select a topic to view the content.';
    }
    document.getElementById('content').innerHTML = content;
}
