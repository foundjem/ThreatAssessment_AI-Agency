# Adversarial Machine Learning Threat Analysis Using Multi-Agent Systems

## Overview

This research project leverages AI-driven multi-agent systems to systematically analyze security threats within the context of adversarial machine learning (AML). The primary objective is to identify, classify, and manage threats effectively by integrating information from diverse sources, such as scientific literature, security databases, and software repositories.

## Project Description

The project introduces AI agents as autonomous computational entities that perform specialized tasks, collaboratively refining queries, extracting and analyzing information, and synthesizing security insights. Each agent dynamically updates its knowledge base to continuously assess and respond to emerging threats in AML, ensuring comprehensive and proactive exploration of the threat landscape.

## AI Agent Capabilities

- **Autonomy:** Operates independently without human intervention.
- **Perception and Interpretation:** Acquires and processes data from multiple, varied sources.
- **Reasoning and Logic:** Refines queries autonomously and makes informed decisions.
- **Continuous Learning:** Dynamically integrates new information to update its internal knowledge base.
- **Classification of AML Threats:** Systematically categorizes adversarial machine learning Tactics, Techniques, and Procedures (TTPs).
- **Visual Representation:** Generates graphical analyses to clearly visualize complex relationships within the ML security landscape.

## Key Components

- **AI Agents:** Autonomous entities designed to carry out specific tasks within the agentic system.
- **Multi-Agent System:** A cooperative framework where multiple AI agents coordinate their specialized roles.
- **Threat Modeling and Classification:** Techniques including data flow diagrams (DFDs), STRIDE, and other frameworks for identifying and categorizing threats.
- **AML Threat Mitigation:** Implementation of security requirements elicitation and countermeasures against identified AML threats.
- **Graphical and Analytical Visualization:** Tools and methodologies for creating visual representations of threat patterns and relationships, enhancing clarity and decision-making capabilities.

## Repository Structure

```
.
├── AI Incident
│   ├── AI_Incident.csv
│   ├── aiatlas.py
│   ├── repo_description.csv
│   └── vuln_crawler_v2.py
├── ATLAS
│   ├── atlas.csv
│   └── atlas2.py
├── Icon\015
├── NVD
│   ├── NVD code
│   │   ├── cwe.py
│   │   └── nvd.py
│   └── NVD tables
│       ├── cwefull.csv
│       └── nvd3.csv
├── Readme.md
├── SuperSet
│   ├── Code
│   │   ├── SupersetTables.py
│   │   ├── Unique dependency name SQL Query
│   │   └── Unique related attacks SQL Query
│   └── Tables
│       ├── AIIncidentsStatistiques.csv
│       ├── AI_Incident_Informations.csv
│       ├── AI_Incident_InformationsTimeLine.csv
│       ├── TacticsUsedByAIIncident.csv
│       ├── TechniquesInGeneralAI.csv
│       ├── uniqueDependencyNames.csv
│       └── uniqueRelatedAttacks.csv
├── agentic_system
│   ├── Academic-databases-search.py
│   ├── GraphAnalysis_linkGitHub2CVEMap.ipynb
│   ├── Multi-agent-RAG.md
│   ├── Multi-agent-RAG.md~
│   ├── advanced_RAG_Reranker.ipynb
│   ├── agentic_solution.ipynb
│   ├── automateRepo_CVE_Extraction.ipynb
│   ├── interactive_ttp_visualization_with_legend.html
│   └── lit-TTPs-graphs.ipynb
├── analysis
│   ├── cwefull-FINAL-fixed-FINAL.csv
│   ├── filtering_sample
│   │   ├── filtering-issues-update.py
│   │   └── grouped_unique_cve_patterns_final_before_after.csv
│   ├── label-nvd
│   │   ├── gpt-classification.py
│   │   ├── nvd-fixed-fixed-FINAL.csv
│   │   ├── output_classified_file_unknown.csv
│   │   └── unknown-cases.csv
│   ├── nvd-before_after_issue_link.csv
│   ├── nvd-before_after_issue_link_reponame.csv
│   ├── nvd-fixed-fixed-FINAL-before_after_issue_link.csv
│   ├── nvd-fixed-fixed-FINAL-before_after_reponame.csv
│   ├── nvd_sample
│   │   ├── FINAL_updated_manual_analysis-issue_link_nvd.csv
│   │   ├── FINAL_updated_manual_analysis_reponame_nvd.csv
│   │   ├── category_occurrences.png
│   │   ├── cpe_dependency_reponame.csv
│   │   ├── cpe_dependency_report_issue.csv
│   │   ├── figure-category-repo.py
│   │   ├── figure-rq3-new.py
│   │   ├── figure-rq3-new2.py
│   │   ├── figure-rq3.py
│   │   ├── figures-repo.py
│   │   ├── figures-repo2.py
│   │   ├── figures.py
│   │   ├── get-attacks_nvd.py
│   │   ├── get-dependencies_nvd.py
│   │   ├── get-repo_nvd.py
│   │   ├── manual_gpt_analysis_bind.py
│   │   ├── nvd-fixed-fixed-FINAL-before_after_issue_link.csv
│   │   ├── nvd-fixed-fixed-FINAL-before_after_reponame.csv
│   │   ├── nvd-threats_issue_link.csv
│   │   ├── nvd-threats_reponame.csv
│   │   ├── related_attacks_count.csv
│   │   ├── target_repos_count.csv
│   │   ├── top_10_related_attacks.png
│   │   ├── top_10_target_repositories.png
│   │   ├── vulnerability_analysis.png
│   │   └── vulnerability_analysis_combined.png
│   └── sample
│       └── issues_github.csv
└── documents
    ├── advisory_repos_vuln_ccm.csv
    ├── advisory_repos_vuln_ccm_x.csv
    ├── datasets.zip
    ├── filtered_repos.csv
    ├── new_attacks.csv
    ├── repos_collection.csv
    ├── repos_wild_vuln_ccm.csv
    ├── ttp_new_attacks.csv
    └── vulnerability_issues.csv

```
- `data/`: Contains datasets from security databases, literature, and codebases.
- `scripts/`: Includes scripts for data processing, querying, and agent operations.
- `models/`: Machine learning models for threat classification and analysis.
- `docs/`: Documentation and research papers related to AML and threat modeling.
- `results/`: Outputs and graphical visualizations from analyses conducted.

## Getting Started



## Dependencies
- Python 3.10+
- PyTorch
- TensorFlow
- NetworkX
- Pandas
- NumPy
- Matplotlib


## License
This project is licensed under the MIT License. 
```md
MIT License

Copyright (c) 2025 -- Armstrong Foundjem

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```



## Contact
For further information, please contact:
- Armstrong Foundjem - foundjem@ieee.org




