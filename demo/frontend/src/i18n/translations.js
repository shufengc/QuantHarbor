export const translations = {
    zh: {
        // Common
        common: {
            save: 'Save',
            cancel: 'Cancel',
            delete: 'Delete',
            load: 'Load',
            confirm: 'Confirm',
            close: 'Close',
            refresh: 'Refresh',
            add: 'Add',
            loading: 'Loading...',
            success: 'Success',
            error: 'Error',
            warning: 'Warning',
            preview: 'Preview',
            download: 'Download',
            underDevelopment: 'Under Development'
        },

        // Landing Page
        landing: {
            title: 'QuantHarbor',
            subtitle: 'AI-Powered Financial Research Platform',
            description1: 'Breaking AI limitations with code agents and deep reasoning',
            description2: 'From data to insights — fully automated, publication-ready financial reports',
            enterButton: 'Enter System',
            slogan: 'AI-Driven Professional Financial Research',
            features: {
                codeAgent: {
                    title: 'Programmable Code Agent',
                    subtitle: 'CAVM Architecture',
                    desc: 'Code-driven execution with variable memory for precise control of heterogeneous data flows'
                },
                vision: {
                    title: 'Vision Enhancement',
                    subtitle: 'VLM-Powered',
                    desc: 'Iterative feedback loops that automatically refine charts to publication-grade quality'
                },
                reasoning: {
                    title: 'Long-Form Reasoning',
                    subtitle: 'Chain-of-Analysis',
                    desc: 'Analyze-then-write framework producing rigorous, coherent in-depth reports'
                },
                research: {
                    title: 'Deep Research',
                    subtitle: 'Evidence-Based',
                    desc: 'Multi-round verification ensuring factual traceability for every conclusion'
                }
            }
        },

        // Header
        header: {
            title: 'QuantHarbor',
            subtitle: 'QuantHarbor AI System',
            controlPanel: 'Control Panel'
        },

        // Menu
        menu: {
            config: 'System Config',
            tasks: 'Task Config',
            execution: 'Execution Monitor',
            reports: 'Reports'
        },

        // Config Page
        config: {
            title: 'System Configuration',
            description: 'Configure system parameters and API keys',
            loadConfig: 'Load Config',
            saveConfig: 'Save Config',
            basicConfig: 'Basic Configuration',
            targetCompany: 'Target Company Name',
            targetCompanyPlaceholder: 'e.g., Apple Inc.',
            targetCompanyRequired: 'Please enter target company name',
            stockCode: 'Stock Code',
            stockCodePlaceholder: 'e.g., AAPL',
            stockCodeRequired: 'Please enter stock code',
            outputDir: 'Output Directory',
            reportTemplatePath: 'Report Template Path',
            outlineTemplatePath: 'Outline Template Path',
            modelConfig: 'Model Configuration',
            modelName: 'Model Name',
            modelNameRequired: 'Please enter model name',
            apiKey: 'API Key',
            apiKeyRequired: 'Please enter API Key',
            baseUrl: 'Base URL',
            baseUrlRequired: 'Please enter Base URL',
            usedModelNames: 'Model Names in Use',
            mainLLM: 'Main LLM Model',
            visionModel: 'Vision Model',
            embeddingModel: 'Embedding Model',
            saveConfigModal: {
                title: 'Save Configuration',
                prompt: 'Enter configuration name:',
                placeholder: 'e.g., Company_Config1'
            },
            loadConfigModal: {
                title: 'Load Configuration',
                empty: 'No saved configurations',
                confirmDelete: 'Confirm Delete',
                confirmDeleteDesc: 'Are you sure you want to delete configuration "{name}"?'
            },
            messages: {
                loadSuccess: 'Configuration "{name}" loaded successfully',
                loadFailed: 'Failed to load configuration',
                saveSuccess: 'Configuration "{name}" saved successfully',
                saveFailed: 'Failed to save configuration',
                updateFailed: 'Failed to update configuration',
                deleteSuccess: 'Configuration "{name}" deleted',
                deleteFailed: 'Failed to delete configuration',
                enterConfigName: 'Please enter configuration name',
                checkForm: 'Please check the form'
            },
            llmLabels: {
                ds: 'DeepSeek LLM',
                vlm: 'Vision LLM',
                embedding: 'Embedding Model'
            }
        },

        // Tasks Page
        tasks: {
            title: 'Task Configuration',
            description: 'Configure data collection and analysis tasks',
            loadTasks: 'Load Tasks',
            saveTasks: 'Save Tasks',
            collectTasks: 'Data Collection Tasks',
            analysisTasks: 'Data Analysis Tasks',
            addTask: 'Add Task',
            dataCollect: 'Collection',
            dataAnalysis: 'Analysis',
            noCollectTasks: 'No data collection tasks',
            noAnalysisTasks: 'No data analysis tasks',
            addTaskModal: {
                collectTitle: 'Add Data Collection Task',
                analysisTitle: 'Add Data Analysis Task',
                collectPlaceholder: 'e.g., Latest share price\nor: Sample company balance sheet',
                analysisPlaceholder: 'e.g., Company history and business review\nor: Ownership structure analysis'
            },
            saveTasksModal: {
                title: 'Save Task Configuration',
                prompt: 'Enter task configuration name:',
                placeholder: 'e.g., Company_TaskConfig1'
            },
            loadTasksModal: {
                title: 'Load Task Configuration',
                empty: 'No saved task configurations',
                confirmDelete: 'Confirm Delete',
                confirmDeleteDesc: 'Are you sure you want to delete task configuration "{name}"?',
                collectCount: 'Collect',
                analysisCount: 'Analyze'
            },
            messages: {
                loadSuccess: 'Task configuration "{name}" loaded successfully',
                loadFailed: 'Failed to load tasks',
                saveSuccess: 'Task configuration "{name}" saved successfully',
                saveFailed: 'Failed to save task configuration',
                updateFailed: 'Failed to update tasks',
                deleteSuccess: 'Task configuration "{name}" deleted',
                deleteFailed: 'Failed to delete task configuration',
                enterTaskName: 'Please enter task configuration name',
                addSuccess: 'Task added successfully',
                deleteTaskSuccess: 'Task deleted successfully',
                enterTaskContent: 'Please enter task content'
            }
        },

        // Execution Page
        execution: {
            title: 'Execution Monitor',
            description: 'Real-time monitoring of Agent execution status and logs',
            start: 'Start Execution',
            resume: 'Resume',
            stop: 'Stop Execution',
            noResumableExecution: 'No resumable execution record',
            resumeTooltip: 'Resume: {name} ({time})',
            lastExecution: 'Last Execution',
            collectTaskCount: '{count} collection tasks',
            analysisTaskCount: '{count} analysis tasks',
            executing: 'Executing',
            executingDesc: 'System is executing tasks, please wait...',
            overview: 'Overview',
            overallProgress: 'Overall Progress',
            currentPhase: 'Current Phase',
            agentType: 'Agent Type',
            taskContent: 'Task Content',
            currentStatus: 'Current Status',
            priority: 'Priority',
            agentId: 'Agent ID',
            executionLogs: 'Execution Logs',
            noLogs: 'No logs',
            showingLogs: 'Showing latest {visible} logs (total {total})',
            noExecutionTasks: 'No execution tasks. Please configure tasks and start execution.',
            taskCount: '{count} tasks',
            status: {
                pending: 'Pending',
                running: 'Running',
                completed: 'Completed',
                error: 'Error'
            },
            phases: {
                1: 'Data Collection Phase',
                2: 'Data Analysis Phase',
                3: 'Report Generation Phase'
            },
            agentTypes: {
                data_collector: 'Data Collector',
                data_analyzer: 'Data Analyzer',
                report_generator: 'Report Generator',
                'deepsearch agent': 'Deep Search'
            },
            messages: {
                startSuccess: 'Execution started',
                stopSent: 'Stop request sent',
                completeSuccess: 'Execution completed',
                executionError: 'Execution error',
                startFailed: 'Failed to start',
                stopFailed: 'Failed to stop'
            }
        },

        // Reports Page
        reports: {
            title: 'Reports',
            description: 'View and download generated analysis reports',
            refresh: 'Refresh',
            totalReports: 'Total Reports',
            targetCompanies: 'Target Companies',
            wordDocs: 'Word Documents',
            markdown: 'Markdown',
            noReports: 'No reports. Please execute tasks to generate reports.',
            totalCount: '{count} reports in total',
            columns: {
                file: 'File',
                type: 'Type',
                targetCompany: 'Target Company',
                size: 'Size',
                modifiedTime: 'Modified Time',
                actions: 'Actions'
            },
            fileTypes: {
                docx: 'Word Document',
                pdf: 'PDF Document',
                md: 'Markdown'
            },
            messages: {
                loadFailed: 'Failed to load reports',
                previewMdOnly: 'Only Markdown files support preview. Please download other formats to view.',
                previewFailed: 'Failed to load preview'
            }
        },

        // Language Switcher
        language: {
            switchTo: 'Switch to English',
            current: 'English'
        }
    },

    en: {
        // Common
        common: {
            save: 'Save',
            cancel: 'Cancel',
            delete: 'Delete',
            load: 'Load',
            confirm: 'Confirm',
            close: 'Close',
            refresh: 'Refresh',
            add: 'Add',
            loading: 'Loading...',
            success: 'Success',
            error: 'Error',
            warning: 'Warning',
            preview: 'Preview',
            download: 'Download',
            underDevelopment: 'Under Development'
        },

        // Landing Page
        landing: {
            title: 'QuantHarbor',
            subtitle: 'AI-Powered Financial Research Platform',
            description1: 'Breaking AI limitations with code agents and deep reasoning',
            description2: 'From data to insights — fully automated, publication-ready financial reports',
            enterButton: 'Enter System',
            slogan: 'AI-Driven Professional Financial Research',
            features: {
                codeAgent: {
                    title: 'Programmable Code Agent',
                    subtitle: 'CAVM Architecture',
                    desc: 'Code-driven execution with variable memory for precise control of heterogeneous data flows'
                },
                vision: {
                    title: 'Vision Enhancement',
                    subtitle: 'VLM-Powered',
                    desc: 'Iterative feedback loops that automatically refine charts to publication-grade quality'
                },
                reasoning: {
                    title: 'Long-Form Reasoning',
                    subtitle: 'Chain-of-Analysis',
                    desc: 'Analyze-then-write framework producing rigorous, coherent in-depth reports'
                },
                research: {
                    title: 'Deep Research',
                    subtitle: 'Evidence-Based',
                    desc: 'Multi-round verification ensuring factual traceability for every conclusion'
                }
            }
        },

        // Header
        header: {
            title: 'QuantHarbor',
            subtitle: 'AI Financial Research Platform',
            controlPanel: 'Control Panel'
        },

        // Menu
        menu: {
            config: 'System Config',
            tasks: 'Task Config',
            execution: 'Execution Monitor',
            reports: 'Reports'
        },

        // Config Page
        config: {
            title: 'System Configuration',
            description: 'Configure system parameters and API keys',
            loadConfig: 'Load Config',
            saveConfig: 'Save Config',
            basicConfig: 'Basic Configuration',
            targetCompany: 'Target Company Name',
            targetCompanyPlaceholder: 'e.g., Apple Inc.',
            targetCompanyRequired: 'Please enter target company name',
            stockCode: 'Stock Code',
            stockCodePlaceholder: 'e.g., AAPL',
            stockCodeRequired: 'Please enter stock code',
            outputDir: 'Output Directory',
            reportTemplatePath: 'Report Template Path',
            outlineTemplatePath: 'Outline Template Path',
            modelConfig: 'Model Configuration',
            modelName: 'Model Name',
            modelNameRequired: 'Please enter model name',
            apiKey: 'API Key',
            apiKeyRequired: 'Please enter API Key',
            baseUrl: 'Base URL',
            baseUrlRequired: 'Please enter Base URL',
            usedModelNames: 'Model Names in Use',
            mainLLM: 'Main LLM Model',
            visionModel: 'Vision Model',
            embeddingModel: 'Embedding Model',
            saveConfigModal: {
                title: 'Save Configuration',
                prompt: 'Enter configuration name:',
                placeholder: 'e.g., Company_Config1'
            },
            loadConfigModal: {
                title: 'Load Configuration',
                empty: 'No saved configurations',
                confirmDelete: 'Confirm Delete',
                confirmDeleteDesc: 'Are you sure you want to delete configuration "{name}"?'
            },
            messages: {
                loadSuccess: 'Configuration "{name}" loaded successfully',
                loadFailed: 'Failed to load configuration',
                saveSuccess: 'Configuration "{name}" saved successfully',
                saveFailed: 'Failed to save configuration',
                updateFailed: 'Failed to update configuration',
                deleteSuccess: 'Configuration "{name}" deleted',
                deleteFailed: 'Failed to delete configuration',
                enterConfigName: 'Please enter configuration name',
                checkForm: 'Please check the form'
            },
            llmLabels: {
                ds: 'DeepSeek LLM',
                vlm: 'Vision LLM',
                embedding: 'Embedding Model'
            }
        },

        // Tasks Page
        tasks: {
            title: 'Task Configuration',
            description: 'Configure data collection and analysis tasks',
            loadTasks: 'Load Tasks',
            saveTasks: 'Save Tasks',
            collectTasks: 'Data Collection Tasks',
            analysisTasks: 'Data Analysis Tasks',
            addTask: 'Add Task',
            dataCollect: 'Collection',
            dataAnalysis: 'Analysis',
            noCollectTasks: 'No data collection tasks',
            noAnalysisTasks: 'No data analysis tasks',
            addTaskModal: {
                collectTitle: 'Add Data Collection Task',
                analysisTitle: 'Add Data Analysis Task',
                collectPlaceholder: 'e.g., Latest share price\nor: Sample company balance sheet',
                analysisPlaceholder: 'e.g., Company history and business review\nor: Ownership structure analysis'
            },
            saveTasksModal: {
                title: 'Save Task Configuration',
                prompt: 'Enter task configuration name:',
                placeholder: 'e.g., Company_TaskConfig1'
            },
            loadTasksModal: {
                title: 'Load Task Configuration',
                empty: 'No saved task configurations',
                confirmDelete: 'Confirm Delete',
                confirmDeleteDesc: 'Are you sure you want to delete task configuration "{name}"?',
                collectCount: 'Collect',
                analysisCount: 'Analyze'
            },
            messages: {
                loadSuccess: 'Task configuration "{name}" loaded successfully',
                loadFailed: 'Failed to load tasks',
                saveSuccess: 'Task configuration "{name}" saved successfully',
                saveFailed: 'Failed to save task configuration',
                updateFailed: 'Failed to update tasks',
                deleteSuccess: 'Task configuration "{name}" deleted',
                deleteFailed: 'Failed to delete task configuration',
                enterTaskName: 'Please enter task configuration name',
                addSuccess: 'Task added successfully',
                deleteTaskSuccess: 'Task deleted successfully',
                enterTaskContent: 'Please enter task content'
            }
        },

        // Execution Page
        execution: {
            title: 'Execution Monitor',
            description: 'Real-time monitoring of Agent execution status and logs',
            start: 'Start Execution',
            resume: 'Resume',
            stop: 'Stop Execution',
            noResumableExecution: 'No resumable execution record',
            resumeTooltip: 'Resume: {name} ({time})',
            lastExecution: 'Last Execution',
            collectTaskCount: '{count} collection tasks',
            analysisTaskCount: '{count} analysis tasks',
            executing: 'Executing',
            executingDesc: 'System is executing tasks, please wait...',
            overview: 'Overview',
            overallProgress: 'Overall Progress',
            currentPhase: 'Current Phase',
            agentType: 'Agent Type',
            taskContent: 'Task Content',
            currentStatus: 'Current Status',
            priority: 'Priority',
            agentId: 'Agent ID',
            executionLogs: 'Execution Logs',
            noLogs: 'No logs',
            showingLogs: 'Showing latest {visible} logs (total {total})',
            noExecutionTasks: 'No execution tasks. Please configure tasks and start execution.',
            taskCount: '{count} tasks',
            status: {
                pending: 'Pending',
                running: 'Running',
                completed: 'Completed',
                error: 'Error'
            },
            phases: {
                1: 'Data Collection Phase',
                2: 'Data Analysis Phase',
                3: 'Report Generation Phase'
            },
            agentTypes: {
                data_collector: 'Data Collector',
                data_analyzer: 'Data Analyzer',
                report_generator: 'Report Generator',
                'deepsearch agent': 'Deep Search'
            },
            messages: {
                startSuccess: 'Execution started',
                stopSent: 'Stop request sent',
                completeSuccess: 'Execution completed',
                executionError: 'Execution error',
                startFailed: 'Failed to start',
                stopFailed: 'Failed to stop'
            }
        },

        // Reports Page
        reports: {
            title: 'Reports',
            description: 'View and download generated analysis reports',
            refresh: 'Refresh',
            totalReports: 'Total Reports',
            targetCompanies: 'Target Companies',
            wordDocs: 'Word Documents',
            markdown: 'Markdown',
            noReports: 'No reports. Please execute tasks to generate reports.',
            totalCount: '{count} reports in total',
            columns: {
                file: 'File',
                type: 'Type',
                targetCompany: 'Target Company',
                size: 'Size',
                modifiedTime: 'Modified Time',
                actions: 'Actions'
            },
            fileTypes: {
                docx: 'Word Document',
                pdf: 'PDF Document',
                md: 'Markdown'
            },
            messages: {
                loadFailed: 'Failed to load reports',
                previewMdOnly: 'Only Markdown files support preview. Please download other formats to view.',
                previewFailed: 'Failed to load preview'
            }
        },

        // Language Switcher
        language: {
            switchTo: 'Switch to English',
            current: 'English'
        }
    }
}
