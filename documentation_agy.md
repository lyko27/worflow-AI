# Antigravity CLI (AGY) — Documentation Complète

---

## Table des Matières / Sommaire

- [**Antigravity CLI Overview**](#antigravity-cli-overview)
  - [Why Antigravity CLI?](#why-antigravity-cli)
    - [Platform comparison](#platform-comparison)
  - [Integration features](#integration-features)
  - [Migrating from Gemini CLI](#migrating-from-gemini-cli)
  - [Next steps](#next-steps)
- [**Getting Started with Antigravity CLI**](#getting-started-with-antigravity-cli)
  - [Roadmap checklist](#roadmap-checklist)
  - [Related resources](#related-resources)
- [**Installation & auth**](#installation-auth)
  - [Installation](#installation)
    - [macOS and Linux](#macos-and-linux)
    - [Windows](#windows)
    - [Installation flags](#installation-flags)
  - [Authentication workflows](#authentication-workflows)
    - [Local silent keyring sign-in](#local-silent-keyring-sign-in)
    - [Remote SSH OAuth flow](#remote-ssh-oauth-flow)
  - [Using a Gemini API key](#using-a-gemini-api-key)
    - [Enable the Gemini API key](#enable-the-gemini-api-key)
    - [Point the CLI to a custom endpoint](#point-the-cli-to-a-custom-endpoint)
    - [Revert to default authentication](#revert-to-default-authentication)
    - [Troubleshooting](#troubleshooting)
  - [Managing your session](#managing-your-session)
    - [Logging out](#logging-out)
  - [Next steps](#next-steps-1)
- [**Antigravity CLI Tutorial**](#antigravity-cli-tutorial)
  - [Overview](#overview)
  - [Step-by-step](#step-by-step)
  - [Next steps](#next-steps-2)
- [**Using AGY CLI**](#using-agy-cli)
    - [Settings](#settings)
    - [Quick Tips](#quick-tips)
    - [Keybindings](#keybindings)
    - [Plugins](#plugins)
    - [Terminal Sandbox](#terminal-sandbox)
    - [CLI Slash Commands Reference](#cli-slash-commands-reference)
    - [Core Slash Commands](#core-slash-commands)
    - [Advanced Customization via `settings.json`](#advanced-customization-via-settingsjson)
    - [Subagents in Antigravity CLI](#subagents-in-antigravity-cli)
    - [Managing Agents: The `/agents` Panel](#managing-agents-the-agents-panel)
  - [Overview](#overview-1)
  - [First-launch onboarding](#first-launch-onboarding)
  - [Converting extensions to plugins](#converting-extensions-to-plugins)
    - [Expected import output](#expected-import-output)
  - [Context files and workspace rules](#context-files-and-workspace-rules)
  - [Updated skills paths](#updated-skills-paths)
  - [MCP config formatting changes](#mcp-config-formatting-changes)
    - [Directory mapping](#directory-mapping)
    - [Required schema updates](#required-schema-updates)
  - [Next steps](#next-steps-3)
- [**Prompting & interaction**](#prompting-interaction)
  - [The prompt box](#the-prompt-box)
    - [Submitting prompts](#submitting-prompts)
    - [Interrupting active sessions](#interrupting-active-sessions)
  - [Multiline composition](#multiline-composition)
    - [Shorthand newline insertions](#shorthand-newline-insertions)
    - [Editing prompts in `$EDITOR`](#editing-prompts-in-$editor)
  - [Attaching media](#attaching-media)
    - [Supported file types](#supported-file-types)
  - [Next steps](#next-steps-4)
- [**Reviewing artifacts**](#reviewing-artifacts)
  - [Collaboration and co-steering](#collaboration-and-co-steering)
  - [Overview of /artifact](#overview-of-artifact)
    - [Interaction keybindings](#interaction-keybindings)
    - [Code files vs visual media](#code-files-vs-visual-media)
  - [Viewing an artifact](#viewing-an-artifact)
    - [Auditing & navigation](#auditing-navigation)
    - [Granular line commenting](#granular-line-commenting)
    - [Custom Mermaid diagram rendering](#custom-mermaid-diagram-rendering)
  - [Next steps](#next-steps-5)
- [**Managing conversations**](#managing-conversations)
  - [Workspace scoping](#workspace-scoping)
  - [Resuming sessions](#resuming-sessions)
  - [Branching with `/fork`](#branching-with-fork)
    - [Forking workflow](#forking-workflow)
  - [Next steps](#next-steps-6)
- [**Choose an execution mode**](#choose-an-execution-mode)
  - [Before you begin](#before-you-begin)
  - [Available modes](#available-modes)
  - [Cycle execution modes during a session](#cycle-execution-modes-during-a-session)
  - [Review modifications in default mode](#review-modifications-in-default-mode)
    - [New file creation previews](#new-file-creation-previews)
  - [Auto-approve edits with accept-edits mode](#auto-approve-edits-with-accept-edits-mode)
  - [Analyze tasks before editing with plan mode](#analyze-tasks-before-editing-with-plan-mode)
  - [Persist or override your default mode](#persist-or-override-your-default-mode)
    - [Using the interactive settings panel](#using-the-interactive-settings-panel)
    - [Setting `agentMode` in `settings.json`](#setting-agentmode-in-settingsjson)
    - [Command-line flag overrides](#command-line-flag-overrides)
  - [Common mistakes](#common-mistakes)
  - [Next steps](#next-steps-7)
- [**Headless mode**](#headless-mode)
  - [Run a single prompt](#run-a-single-prompt)
  - [Output formats](#output-formats)
    - [Text](#text)
    - [JSON](#json)
    - [Streaming JSON](#streaming-json)
  - [Parse output with jq](#parse-output-with-jq)
  - [Continue a conversation](#continue-a-conversation)
  - [Select a model, effort, or agent](#select-a-model-effort-or-agent)
  - [Permissions in headless mode](#permissions-in-headless-mode)
  - [Handle exit codes and errors](#handle-exit-codes-and-errors)
  - [Flag reference](#flag-reference)
  - [Example: run the agent in CI](#example-run-the-agent-in-ci)
  - [Next steps](#next-steps-8)
- [**Background tasks & subagents**](#background-tasks-subagents)
  - [Asynchronous execution model](#asynchronous-execution-model)
  - [Managing agents: The `/agents` panel](#managing-agents-the-agents-panel-1)
    - [Opening the panel](#opening-the-panel)
    - [Panel overview](#panel-overview)
  - [Custom Agents (Markdown Format)](#custom-agents-markdown-format)
  - [Deep-dive monitoring](#deep-dive-monitoring)
  - [Monitoring background tasks with `/tasks`](#monitoring-background-tasks-with-tasks)
  - [Keyboard ergonomics](#keyboard-ergonomics)
    - [Detailed “Teleport” navigation (`Alt+J`)](#detailed-“teleport”-navigation-altj)
    - [”Fast-Path” confirmations (`Ctrl+K`)](#”fast-path”-confirmations-ctrlk)
  - [Next steps](#next-steps-9)
- [**Sandbox**](#sandbox)
  - [The security model](#the-security-model)
    - [Native OS containment](#native-os-containment)
  - [Activating the sandbox](#activating-the-sandbox)
    - [Sandbox configurations](#sandbox-configurations)
  - [Interactive approvals with sandbox](#interactive-approvals-with-sandbox)
  - [See also](#see-also)
- [**Permissions**](#permissions)
  - [Fine-grained permissions](#fine-grained-permissions)
  - [Supported actions & matching rules](#supported-actions-matching-rules)
    - [Global wildcard syntax](#global-wildcard-syntax)
    - [Implicit permission rules](#implicit-permission-rules)
    - [Cross-platform path normalization](#cross-platform-path-normalization)
  - [Default system behaviors & guardrails](#default-system-behaviors-guardrails)
  - [Interactive permission prompts](#interactive-permission-prompts)
  - [Configuration examples](#configuration-examples)
  - [See also](#see-also-1)
- [**Projects**](#projects)
  - [Launching sessions with projects](#launching-sessions-with-projects)
    - [1\. Default project execution](#1\-default-project-execution)
    - [2\. Opening a session in a specific project](#2\-opening-a-session-in-a-specific-project)
    - [3\. Creating a new project on startup](#3\-creating-a-new-project-on-startup)
    - [4\. Resuming an existing conversation](#4\-resuming-an-existing-conversation)
  - [Moving conversations between projects (`/fork`)](#moving-conversations-between-projects-fork)
- [**Settings, rendering & keybindings**](#settings-rendering-keybindings)
  - [Setting up preferences](#setting-up-preferences)
    - [Configuration file location](#configuration-file-location)
    - [The interactive settings panel](#the-interactive-settings-panel)
  - [Command-line overrides](#command-line-overrides)
  - [Visual rendering modes](#visual-rendering-modes)
    - [Alt-screen mode (`always`)](#alt-screen-mode-always)
    - [Inline mode (`never`)](#inline-mode-never)
  - [Configuration options reference](#configuration-options-reference)
    - [Safety & permissions](#safety-permissions)
    - [Display & rendering](#display-rendering)
    - [Editor & notifications](#editor-notifications)
    - [AI Credits & Feedback](#ai-credits-feedback)
  - [Custom status lines & terminal titles](#custom-status-lines-terminal-titles)
  - [Keybindings configuration](#keybindings-configuration)
    - [Keybindings file location](#keybindings-file-location)
    - [Format and customization](#format-and-customization)
    - [Restoring defaults](#restoring-defaults)
  - [Next steps](#next-steps-10)
- [**Vim editor mode**](#vim-editor-mode)
  - [Enable Vim editor mode](#enable-vim-editor-mode)
    - [Using the settings panel](#using-the-settings-panel)
    - [Using `settings.json`](#using-settingsjson)
  - [Switch between modes](#switch-between-modes)
  - [Submit your prompt](#submit-your-prompt)
    - [Start in Insert mode](#start-in-insert-mode)
  - [Move the cursor](#move-the-cursor)
  - [Edit text](#edit-text)
    - [Single-key commands](#single-key-commands)
    - [Operators and motions](#operators-and-motions)
    - [Text objects](#text-objects)
  - [Work with selections](#work-with-selections)
  - [Run slash and shell commands](#run-slash-and-shell-commands)
  - [Customize the submit and newline keys](#customize-the-submit-and-newline-keys)
    - [Submit with Enter in NORMAL mode only](#submit-with-enter-in-normal-mode-only)
    - [Submit with Enter in INSERT mode too](#submit-with-enter-in-insert-mode-too)
  - [Show the mode in a custom status line](#show-the-mode-in-a-custom-status-line)
  - [Next steps](#next-steps-11)
- [**Managing AI Credits & Quotas**](#managing-ai-credits-quotas)
  - [Quota Tracking](#quota-tracking)
  - [Slash Commands & Managing Balance](#slash-commands-managing-balance)
  - [Settings Configuration](#settings-configuration)
  - [See also](#see-also-2)
- [**Model Context Protocol (MCP)**](#model-context-protocol-mcp)
  - [What is MCP?](#what-is-mcp)
    - [Add Context](#add-context)
    - [Add Custom Tools](#add-custom-tools)
  - [Antigravity 2.0](#antigravity-20)
  - [Antigravity IDE](#antigravity-ide)
  - [Antigravity CLI](#antigravity-cli)
    - [Interactive MCP Manager](#interactive-mcp-manager)
    - [Global and Workspace Server Configs](#global-and-workspace-server-configs)
  - [Antigravity SDK](#antigravity-sdk)
  - [MCP Configuration Structure](#mcp-configuration-structure)
    - [MCP Configuration Properties](#mcp-configuration-properties)
  - [MCP Authentication](#mcp-authentication)
    - [Google Credentials](#google-credentials)
    - [OAuth](#oauth)
    - [Custom Headers](#custom-headers)
  - [MCP Permissions and Access Control](#mcp-permissions-and-access-control)
  - [Supported MCP Servers](#supported-mcp-servers)
- [**Plugins & skills**](#plugins-skills)
  - [The extensibility model](#the-extensibility-model)
  - [Antigravity plugins](#antigravity-plugins)
    - [Plugin filesystem structure](#plugin-filesystem-structure)
    - [The plugin manifest (plugin.json)](#the-plugin-manifest-pluginjson)
    - [Managing plugins via CLI subcommands](#managing-plugins-via-cli-subcommands)
  - [Agent skills](#agent-skills)
    - [Creating local workspace skills](#creating-local-workspace-skills)
    - [Sharing global skills](#sharing-global-skills)
  - [Managing hooks](#managing-hooks)
  - [Model Context Protocol (MCP)](#model-context-protocol-mcp-1)
  - [Next steps](#next-steps-12)
- [**Status line customization**](#status-line-customization)
  - [Overview](#overview-2)
  - [Custom status line scripting](#custom-status-line-scripting)
    - [Configuration](#configuration)
    - [Available JSON fields](#available-json-fields)
    - [JSON payload example](#json-payload-example)
    - [Example script](#example-script)
  - [See also](#see-also-3)
- [**Terminal title customization**](#terminal-title-customization)
  - [Overview](#overview-3)
  - [Custom title scripting](#custom-title-scripting)
    - [Configuration](#configuration-1)
    - [JSON state payload schema](#json-state-payload-schema)
    - [Example script](#example-script-1)
  - [See also](#see-also-4)
- [**Agents Command (/agents)**](#agents-command-agents)
  - [Before you begin](#before-you-begin-1)
  - [Overview](#overview-4)
  - [Custom Agent Selection & Discovery](#custom-agent-selection-discovery)
    - [1\. Switching between agents](#1\-switching-between-agents)
    - [2\. Creating custom agents](#2\-creating-custom-agents)
  - [Subagent Monitoring & Control](#subagent-monitoring-control)
    - [1\. Inspecting subagent progress](#1\-inspecting-subagent-progress)
    - [2\. Terminating active subagents](#2\-terminating-active-subagents)
    - [3\. Inline tool approvals](#3\-inline-tool-approvals)
  - [Panel Keybindings Reference](#panel-keybindings-reference)
  - [Common mistakes](#common-mistakes-1)
  - [Next steps](#next-steps-13)
- [**Code Search Command (/codesearch)**](#code-search-command-codesearch)
  - [Overview](#overview-5)
  - [Running a search](#running-a-search)
    - [Navigation and controls](#navigation-and-controls)
  - [Query syntax](#query-syntax)
    - [Literal (fixed-string) matching](#literal-fixed-string-matching)
    - [Filtering by file path](#filtering-by-file-path)
  - [Opening a file and commenting on lines](#opening-a-file-and-commenting-on-lines)
    - [Open a result](#open-a-result)
    - [Comment on a specific line](#comment-on-a-specific-line)
    - [Send your comments to the agent](#send-your-comments-to-the-agent)
  - [Next steps](#next-steps-14)
- [**AI Credits Command (/credits)**](#ai-credits-command-credits)
  - [Overview](#overview-6)
  - [Using the Credits Command](#using-the-credits-command)
  - [Next steps](#next-steps-15)
- [**Diff Command (/diff)**](#diff-command-diff)
  - [Overview](#overview-7)
  - [Interactive Diff Viewer Panels](#interactive-diff-viewer-panels)
    - [Navigation and Controls](#navigation-and-controls-1)
  - [Step-by-Step Walkthrough](#step-by-step-walkthrough)
    - [1\. Reviewing Workspace Changes (VCS Mode)](#1\-reviewing-workspace-changes-vcs-mode)
    - [2\. Adding Comments and Steering the Agent](#2\-adding-comments-and-steering-the-agent)
    - [3\. Reviewing Turn History (Turn Mode)](#3\-reviewing-turn-history-turn-mode)
    - [4\. Navigating the Commit Tree (Commit Mode)](#4\-navigating-the-commit-tree-commit-mode)
  - [Keyboard Shortcuts Reference](#keyboard-shortcuts-reference)
    - [File List View (VCS & Turn Modes)](#file-list-view-vcs-turn-modes)
    - [File Detail View](#file-detail-view)
    - [Commit Tree View (Commit Mode)](#commit-tree-view-commit-mode)
    - [Exit Confirmation Screen](#exit-confirmation-screen)
  - [See also](#see-also-5)
- [**Permissions Command (/permissions)**](#permissions-command-permissions)
  - [Overview](#overview-8)
  - [Managing permissions interactively](#managing-permissions-interactively)
    - [Navigation and controls](#navigation-and-controls-2)
  - [Step-by-step walkthrough](#step-by-step-walkthrough-1)
    - [1\. Selecting a scope and viewing rules](#1\-selecting-a-scope-and-viewing-rules)
    - [2\. Adding a permission rule](#2\-adding-a-permission-rule)
    - [3\. Editing a permission rule](#3\-editing-a-permission-rule)
    - [4\. Deleting a permission rule](#4\-deleting-a-permission-rule)
  - [Next steps](#next-steps-16)
- [**Resume Command (/resume)**](#resume-command-resume)
  - [Overview](#overview-9)
  - [Interactive Session Picker](#interactive-session-picker)
    - [1\. Navigating and Searching Conversations](#1\-navigating-and-searching-conversations)
    - [2\. Renaming a Conversation](#2\-renaming-a-conversation)
    - [3\. Deleting a Conversation](#3\-deleting-a-conversation)
    - [4\. Importing from Antigravity 2.0](#4\-importing-from-antigravity-20)
  - [Command-Line Shortcuts](#command-line-shortcuts)
    - [Quick Resume Last Session (`-c` / `--continue`)](#quick-resume-last-session-c-continue)
    - [Resume Specific Session (`--conversation`)](#resume-specific-session-conversation)
  - [Under the Hood: The Session Cache](#under-the-hood-the-session-cache)
    - [The Cache File](#the-cache-file)
    - [Resolution Workflow](#resolution-workflow)
  - [See also](#see-also-6)
- [**Status Line Command (/statusline)**](#status-line-command-statusline)
  - [Overview](#overview-10)
  - [Usage](#usage)
    - [Toggle Status Line](#toggle-status-line)
    - [Enable or Disable Explicitly](#enable-or-disable-explicitly)
    - [Configure a Custom Command](#configure-a-custom-command)
    - [Revert to Default](#revert-to-default)
    - [Show Help](#show-help)
  - [Next steps](#next-steps-17)
- [**Window Title Command (/title)**](#window-title-command-title)
  - [Overview](#overview-11)
  - [Interactive Toggling](#interactive-toggling)
  - [Next steps](#next-steps-18)
- [**Model Quotas (/usage)**](#model-quotas-usage)
  - [Overview](#overview-12)
  - [Viewing your usage](#viewing-your-usage)
    - [Interactive Panel Features](#interactive-panel-features)
    - [Navigation Controls](#navigation-controls)
  - [Next steps](#next-steps-19)
- [**Best practices for Antigravity CLI**](#best-practices-for-antigravity-cli)
  - [Establish verification loops](#establish-verification-loops)
  - [Explore, plan, then execute](#explore-plan-then-execute)
  - [Enrich your prompting context](#enrich-your-prompting-context)
    - [Target file autocompletion](#target-file-autocompletion)
    - [Attaching visual evidence](#attaching-visual-evidence)
  - [Configure your workspace environment](#configure-your-workspace-environment)
    - [Write a codebase rule file](#write-a-codebase-rule-file)
    - [Establish structured permissions](#establish-structured-permissions)
  - [Manage TUI sessions proactively](#manage-tui-sessions-proactively)
    - [Course-correct early (`esc`)](#course-correct-early-esc)
    - [Rewind history with `/rewind`](#rewind-history-with-rewind)
    - [Branch experiments with `/fork`](#branch-experiments-with-fork)
  - [Automate and script](#automate-and-script)
    - [Run non-interactive commands (`-p`)](#run-non-interactive-commands-p)
    - [Fan out using parallel subagents](#fan-out-using-parallel-subagents)
  - [Related resources](#related-resources-1)
- [**Troubleshooting**](#troubleshooting-1)
  - [Quick reference](#quick-reference)
  - [Configure your shell PATH](#configure-your-shell-path)
    - [Symptom](#symptom)
    - [Cause](#cause)
    - [Resolution](#resolution)
  - [Authorize keyring permissions](#authorize-keyring-permissions)
    - [Symptom](#symptom-1)
    - [Cause](#cause-1)
    - [Resolution](#resolution-1)
  - [Enable emulator clipboard forwarding](#enable-emulator-clipboard-forwarding)
    - [Symptom](#symptom-2)
    - [Cause](#cause-2)
    - [Resolution](#resolution-2)
  - [Resolve self-updater locks and failures](#resolve-self-updater-locks-and-failures)
    - [Symptom](#symptom-3)
    - [Cause](#cause-3)
    - [Resolution](#resolution-3)
  - [Next steps](#next-steps-20)
- [**CLI reference**](#cli-reference)
  - [Core slash commands](#core-slash-commands-1)
  - [Default keybindings](#default-keybindings)
    - [Global controls](#global-controls)
    - [Prompt focus keys](#prompt-focus-keys)
    - [Navigation & scrolling](#navigation-scrolling)
    - [Tool confirmations](#tool-confirmations)
  - [Configuration keys (`settings.json`)](#configuration-keys-settingsjson)
    - [Example `settings.json`](#example-settingsjson)
  - [Next steps](#next-steps-21)

---
# Antigravity CLI Overview

The Antigravity CLI is the lightweight Terminal User Interface (TUI) surface of Antigravity. It brings the same core agentic capabilities as Antigravity 2.0 (such as multi-step reasoning, multi-file editing, tool calling, and conversation history) directly to your terminal.

## Why Antigravity CLI?

Antigravity CLI brings the reasoning, execution, and orchestration capabilities of our shared agent harness directly into your local shell. While Antigravity 2.0 offers a comprehensive visual editor interface, the CLI is custom-built for speed, lightweight operation, and seamless integration with terminal-first workflows.

### Platform comparison

| Feature | Antigravity CLI | Antigravity 2.0 |
| --- | --- | --- |
| **Primary interface** | Keyboard-driven TUI | Visual desktop editor / IDE |
| **Performance overhead** | Near-zero, extremely lightweight | Standard desktop IDE footprint |
| **Workflow focus** | Fast local iterations, SSH, headless | Complete project management, visual workspace |
| **Navigation** | Universal keyboard shortcuts | Mouse and multi-panel layout |
| **Remote usability** | Native SSH, tmux, and terminal multiplexers | Local workspace or remote development containers |

## Integration features

Antigravity CLI operates in tandem with Antigravity 2.0, sharing configurations and enabling frictionless transitions between interfaces:

*   **Shared agent harness**: Both environments run on the exact same agent core. Any enhancements to multi-step reasoning, tool usage, or code comprehension apply across both platforms.
*   **Shared settings sync**: Your core preferences, permissions, and security configurations synchronize automatically across both interfaces. Updating a permission rule or standard configuration in one platform immediately updates the other.
*   **Conversation export**: Seamlessly move active conversations between platforms. If a terminal session grows in complexity and requires visual orchestration, export the conversation to Antigravity 2.0 to continue with the visual editor interface.

## Migrating from Gemini CLI

If you are transitioning from Gemini CLI, the onboarding process supports a one-time import to automatically migrate your existing Gemini CLI extensions, skills, and settings. To learn more, read [Migrating from Gemini CLI](/docs/cli/gcli-migration).

## Next steps

Explore the guides below to set up your environment and begin working with autonomous agents:

*   **[Installation & Auth](/docs/cli/install)**: Set up the CLI, configure enterprise parameters, and complete silent authentication.
*   **[Getting Started](/docs/cli/getting-started)**: Explore the onboarding roadmap, first-launch setups, and core conceptual models.
*   **[Tutorial](/docs/cli/tutorial)**: Run your first multi-file generation task with an active agent.
*   **[Prompting & Interaction](/docs/cli/prompting)**: Master multiline composing, prompt editing, and pasting terminal media.
*   **[Reviewing Artifacts](/docs/cli/artifacts)**: Leverage transparency and review agent plans, diffs, and test runs.
*   **[AI Credits](/docs/cli/credits)**: Configure and monitor AI Premium credits fallback, pricing links, and settings.
*   **[Plugins & Skills](/docs/cli/plugins)**: Create your own custom skills slash commands, manage hooks, and configure MCP servers.
*   **[Best Practices](/docs/cli/best-practices)**: Master workflow pipelines, verification loops, and session course-corrections.

# Getting Started with Antigravity CLI

Welcome to Antigravity CLI! This guide provides a direct, high-level developer roadmap to install the client, launch the Terminal User Interface (TUI), and begin collaborating with autonomous agents.

## Roadmap checklist

Complete the following sequential steps to launch your first session:

1.  **Install the client (fast path)**
    
    Run the appropriate fast-path command for your operating system:
    
    **macOS / Linux**:
    
    ```
    curl -fsSL https://antigravity.google/cli/install.sh | bash
    ```
    
    **Windows (PowerShell)**:
    
    ```
    irm https://antigravity.google/cli/install.ps1 | iex
    ```
    
    **Windows (CMD)**:
    
    ```
    curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
    ```
    
    By default, the installer registers the `agy` binary to your platform-specific directory:
    
    *   **macOS / Linux**: `~/.local/bin/agy`
    *   **Windows**: `C:\Users\<username>\AppData\Local\agy\bin` (where `<username>` represents your active Windows profile name).
    
> **Note**: Advanced Setup**: For detailed enterprise credentials configuration, secure keyring auth permissions, proxy setups, or troubleshooting installation issues, consult the **[Installation & Auth Guide](/docs/cli/install)**.
    
2.  **Launch the TUI inside a project**
    
    Open a fresh terminal window, navigate to your target project codebase directory, and execute the launcher command:
    
    ```
    agy
    ```
    
3.  **Complete the first-launch setup**
    
    On your very first launch, the TUI walks you through a brief interactive setup:
    
    *   **Color Scheme**: Select your preferred visual theme (Solarized, Dark, Solarized Light, or standard Terminal colors).
    *   **Rendering Mode**: Choose Alt-Screen mode (alternate buffer with full-screen scrolling) or Inline mode (sequential stream integrated with your terminal’s history).
    *   **Workspace Trust**: Confirm that you trust the repository directory. Once confirmed, the agent indexes the files and stands ready.
4.  **Run your first agent task**
    
    Type the following instruction in the prompt box at the bottom of your TUI screen and press Enter:
    
    ```
    Write a simple python script to fetch web page text
    ```
    
    The agent reads the workspace, reasons about the task, and proposes a plan. For a detailed step-by-step tutorial on reviewing code and running test commands inside the TUI, follow the **[Tutorial Guide](/docs/cli/tutorial)**.
    

## Related resources

Optimize your local environment configurations and master advanced collaboration tools:

*   **[Best Practices](/docs/cli/best-practices)**: Master verification loops, planning phases, rule files, and session checkpoints.
*   **[Troubleshooting](/docs/cli/troubleshooting)**: Resolve common path, keyring, or SSH forwarding errors.
*   **[CLI Reference](/docs/cli/reference)**: Dense reference sheets cataloging all slash commands, shortcuts, and JSON keys.

# Installation & auth

Install Antigravity CLI, configure enterprise requirements, and establish secure authenticated sessions.

## Installation

Antigravity CLI runs natively on macOS, Linux, and Windows. Use the platform-specific scripts below to install or upgrade the binary on your system.

### macOS and Linux

Execute the native installer script to download and install the executable to `~/.local/bin/agy`:

```
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

### Windows

The installation script registers the `agy` binary to your local user directory: `C:\Users\<username>\AppData\Local\agy\bin` (where `<username>` represents your active Windows user profile).

**PowerShell**: Open PowerShell and execute the following installation script:

```
irm https://antigravity.google/cli/install.ps1 | iex
```

**CMD**: Open a standard Command Prompt and execute:

```
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
```

### Installation flags

When executing the installation scripts, you can append the following customization flags:

*   `--skip-aliases`: Bypasses shell profile alias purging (prevents the script from purging or updating legacy `agy` or `antigravity` shell aliases).
*   `--skip-path`: Bypasses shell profile `PATH` appending (prevents the script from modifying your shell profile’s dynamic environment variables).

## Authentication workflows

Antigravity CLI uses secure credentials and token profiles to communicate with the shared agent harness.

### Local silent keyring sign-in

When launching `agy` on your local machine, the CLI attempts to access your operating system’s native secure keyring (such as Apple Keychain, Linux Secret Service/dbus, or Windows Credential Manager). If a valid token profile is found, the CLI authenticates your session silently without opening a browser.

If no saved session is found:

1.  The CLI automatically launches your local default web browser.
2.  Sign in using your approved account credentials.

### Remote SSH OAuth flow

When running over SSH, the CLI detects the remote connection environment. Because it cannot launch a local web browser, the CLI initiates a manual URL loop:

1.  Launch `agy` in your remote terminal session.
2.  The CLI detects the SSH environment and prints a unique, secure authorization URL.
3.  Copy this URL and paste it into a web browser on your local machine.
4.  Sign in with your approved credentials and complete the authentication.
5.  The browser displays a unique alphanumeric authorization code.
6.  Copy this code, return to your remote SSH terminal, and paste it into the prompt.

## Using a Gemini API key

Run Antigravity CLI with your own Gemini API key instead of a signed-in Google account. Model requests go directly to the Gemini API, and the CLI never establishes an account session. This suits headless and CI runs, where no browser is available to complete a sign-in. Create a key in [Google AI Studio](https://aistudio.google.com/app/api-keys).

To use a Gemini API key, you have to set a provider and an environment variable with the API key. Only setting a `GEMINI_API_KEY` environment variable on its own has no effect.

### Enable the Gemini API key

1.  Set `modelProvider` to `gemini` in `~/.gemini/antigravity-cli/settings.json`:
    
    ```
    {
        "modelProvider": "gemini"
    }
    ```
    
2.  Export your key as `GEMINI_API_KEY`:
    
    ```
    export GEMINI_API_KEY="your-api-key"
    ```
    
    This applies to the current shell only. Add the same line to your shell profile, such as `~/.zshrc` or `~/.bashrc`, to persist it across sessions.
    
3.  Start the CLI:
    
    ```
    agy
    ```
    

The CLI skips the sign-in screen and opens the main interface directly. The header shows **Gemini API key** instead of your account email:

![Antigravity CLI authenticated with a Gemini API key, with "Gemini API key" shown in the header in place of an account email](/assets/image/docs/cli/install-gemini-api-key.png)

> **Note:** When you use the authentication with a `GEMINI_API_KEY`, `/logout` has no effect because there is no stored session to clear.

### Point the CLI to a custom endpoint

To send model requests to a different Gemini-compatible endpoint, set the `GOOGLE_GEMINI_BASE_URL` environment variable:

```
export GOOGLE_GEMINI_BASE_URL="https://your-endpoint.example.com"
```

### Revert to default authentication

If you want to revert back to using the default account based authentication:

1.  Remove `modelProvider` from `~/.gemini/antigravity-cli/settings.json`.
2.  Restart the CLI to sign in to your account.

> **Note:** The CLI cannot start if you unset the `GEMINI_API_KEY` environment variable, but still have the `modelProvider` set to `gemini`.

### Troubleshooting

| Symptom | Cause | Resolution |
| --- | --- | --- |
| The CLI exits at startup reporting that `GEMINI_API_KEY` is not set | `modelProvider` is `gemini` but the key is missing from the environment | Export `GEMINI_API_KEY`, or remove `modelProvider` to use the default authentication |
| The CLI signs in normally and ignores the setting | `modelProvider` holds an unrecognized value | `gemini` is the only accepted value. Check the spelling and restart the CLI |
| A key set through `GOOGLE_API_KEY` or a `.env` file has no effect | The CLI reads the credential only from `GEMINI_API_KEY` in the environment, and does not load `.env` files | Export `GEMINI_API_KEY` in your shell or shell profile |
| Requests fail mid-session with a generic model error | The key is invalid, revoked, or lacks access to the requested model | Verify the key in Google AI Studio. The CLI checks only that the key is non-empty at startup, so an unusable key only surfaces on the first conversation |

## Managing your session

Terminating your session clears active credentials and local cache directories.

### Logging out

To disconnect your account and purge saved authentication profiles from your operating system’s keyring, run the following command in the CLI prompt box:

```
/logout
```

## Next steps

Once you complete installation and authentication, start interacting with your local agent:

*   **[Tutorial](/docs/cli/tutorial)**: Create and run a basic Python project with an agent.
*   **[Prompting & Interaction](/docs/cli/prompting)**: Explore multiline text editing, interrupt commands, and terminal media pasting.
*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Configure secure filesystem directories and command limits.

# Antigravity CLI Tutorial

Learn how to launch Antigravity CLI, collaborate with an autonomous local agent, review generated files, and execute terminal test commands.

## Overview

This guide walks you through a rapid onboarding exercise. You will direct an autonomous agent to create a Python utility script, review the changes, and verify its execution.

## Step-by-step

1.  **Create a clean project directory and launch the Antigravity TUI**
    
    ```
    mkdir agy-demo && cd agy-demo
    agy
    ```
    
> **Note**: First Launch**: If running `agy` for the first time, follow the terminal instructions to complete silent authentication. See [Installation & Auth](/docs/cli/install) for troubleshooting details.
    
2.  **Prompt the agent to generate a Python scraping script**
    
    Type the following instruction in the prompt box at the bottom of your screen and press Enter:
    
    ```
    Write a simple python script to fetch web page text
    ```
    
    The agent reads the workspace, determines that no files exist, and formulates a plan to create a script. You will see real-time updates as the agent performs reasoning and schedules actions.
    
3.  **Open the artifact review screen to inspect the proposed code**
    
    Once the agent finishes generating the file, a notification appears. Press Ctrl + R to enter the **Artifact Review** screen.
    
    *   Navigate to the newly created `main.py` using ↑/↓.
    *   Review the complete file content and diff.
    *   Press Y to approve the creation of `main.py`.
    *   Press Esc to close the review panel and return to the primary prompt.
4.  **Execute a test command with the agent to verify the output**
    
    Direct the agent to run the Python script to verify its behavior. Type the following command in the prompt box and press Enter:
    
    ```
    Run the python script and show me the output
    ```
    
    The agent proposes to run `python3 main.py`. Press Y to confirm and execute the command. The agent runs the script locally and streams the standard output directly into your terminal screen.
    
5.  **Exit the Antigravity session**
    
    Once you complete your task, press Ctrl + D (or type `/exit`) in the prompt box to close the TUI and restore your original shell session.
    

## Next steps

Now that you have executed your first agent-assisted workflow, learn how to configure the CLI and master core concepts:

*   **[Installation & Auth](/docs/cli/install)**: Detailed instructions on installing `agy` and setting up SSH profiles.
*   **[Prompting & Interaction](/docs/cli/prompting)**: Best practices for multiline inputs, pasting media files, and active interrupt controls.
*   **[Reviewing Artifacts](/docs/cli/artifacts)**: Deep dive into the “Trust through Transparency” architectural pattern.

# Using AGY CLI

### Settings

Antigravity CLI provides a flexible configuration system to customize workspace behavior, safety restrictions, editor preferences, visual style, and performance.

*   **Configuration File**: Stored in a plain JSON file `~/.gemini/antigravity-cli/settings.json`.
*   **Settings Panel**: Type `/config` or `/settings` to open a full-screen overlay menu listing all available options.
    *   Select a setting to open its list of options or a text input field.
    *   Immediately save your selection to the disk and return to the main list.
*   **Overrides**: Certain settings can be overridden at launch via CLI flags (e.g., `--sandbox` or `--dangerously-skip-permissions`).
    *   The settings menu will display an indicator showing where the override came from (e.g., _Sandbox Mode on overridden by `--sandbox`_).
    *   You can still edit the persistent setting on disk, but the current session will enforce the command-line override until restarted.

### Quick Tips

| Action/Feature | Tip/Command |
| :-- | :-- |
| **Auto-complete to file paths** | `@` will trigger path suggestions |
| **Clear Prompt** | Type `esc esc` to clear your prompt box (when no streaming is active) |
| **Terminal Commands** | Use `!` at the start of your prompt to run terminal commands directly |
| **Help** | Type `?` to get help and list all slash commands |
| **Reduce Noise from Tool Calls** | Set verbosity to **low** in `/config` to minimize outputs from numerous tool calls |
| **Manage Permissions** | Control permissions via `/config` or `/permissions` |
| **Go Back in Conversation** | Use `/rewind` or `/undo` to rewind the conversation history |
| **Fork Conversation** | Use `/fork` to spin up a separate workspace and branch the conversation from an earlier point |
| **Clear Conversation** | Use `/clear` to clear the prompt and start a new conversation session |
| **Resume Conversation** | Use `/resume` to list and resume previous conversation logs |
| **Auto-Save Resume** | When you close the CLI, it automatically prints the exact command needed to resume that specific session |

### Keybindings

AGY CLI allows for custom keybindings. You can edit them by typing `/keybindings` or modifying the JSON file directly.

*   **File Location**: `~/.gemini/antigravity-cli/keybindings.json`.
*   **Reset**: To reset to default, delete the `keybindings.json` file.

**Default Keybindings**

| Action/Command | Keys | Purpose |
| :-- | :-- | :-- |
| **Clear TUI Screen** | `ctrl+l` | Clear terminal output |
| **Enter / Submit** | `enter` | Submit prompts or choices |
| **Escape / Cancel** | `ctrl+c`, `esc` | Stop stream, close menus, or clear prompt |
| **Exit CLI** | `ctrl+d` | Terminate CLI TUI session |
| **Suspend CLI** | `ctrl+z` | Push CLI session to terminal background |
| **Edit Command** | `e` | Open editor to edit proposed terminal command |
| **Confirm No** | `n` | Decline terminal command execution |
| **Confirm Yes** | `y` | Approve terminal command execution |
| **Open Editor** | `ctrl+g` | Edit prompt inside your default shell editor |
| **Paste Text** | `ctrl+v` | Paste text from your clipboard |
| **Redo Text Edit** | `ctrl+shift+z` | Redo last undone text change |
| **Undo Text Edit** | `ctrl+_`, `ctrl+shift+-` | Undo last text change |
| **Yank (Copy)** | `ctrl+y` | Yank/copy selected text |
| **Navigate Down** | `down` | Scroll down in menu lists |
| **Go to Bottom** | `ctrl+end` | Jump TUI view directly to the bottom |
| **Go to Top** | `ctrl+home` | Jump TUI view directly to the top |
| **Navigate Left** | `left` | Move prompt cursor left |
| **Page Down** | `pgdown`, `shift+down` | Scroll TUI page down |
| **Page Up** | `pgup`, `shift+up` | Scroll TUI page up |
| **Navigate Right** | `right` | Move prompt cursor right |
| **Tab / Focus** | `tab` | Auto-complete choices or switch component focus |
| **Navigate Up** | `up` | Scroll up in menu lists |
| **Insert Newline** | `alt+enter`, `ctrl+j`, `shift+enter` | Add newline to prompt without submitting |

You can map a single action to many keybindings in the JSON file. To disable keybindings, set the list to empty (e.g., `[]`). If the file is malformed, the CLI will use the valid parts and fall back to defaults for the broken actions.

> **Note**: Important**: Keybindings `cli.exit` and `cli.enter` cannot be disabled.# Antigravity CLI Features

### Plugins

**How Plugins Work**  
Plugins are namespaced bundles that can contain skills, agents, rules, MCP servers, and hooks as a single deployable unit.

When you install a plugin, the CLI stages the files in your home directory under `~/.gemini/antigravity-cli/plugins/<plugin_name>/`. The Antigravity Agent automatically discovers and loads these staged customizations.

```
~/.gemini/antigravity-cli/
├── plugins/
│   └── <plugin_name>/
│       ├── plugin.json         # Required marker file
│       ├── mcp_config.json     # Optional MCP server definitions
│       ├── hooks.json          # Optional event hooks definition
│       ├── skills/             # Optional skills
│       ├── agents/             # Optional subagents
│       └── rules/              # Optional rules
└── import_manifest.json        # Tracking manifest
```

**Accessing Plugin Components**  
Once staged and loaded, you can interact with the plugin components inside the CLI using slash commands.

### Terminal Sandbox

The Terminal Sandbox is a lightweight security isolation mechanism that protects your host system from potentially destructive file manipulations or unauthorized outbound network requests when the agent executes local shell commands.

Rather than running heavy virtual machines or containers, the CLI leverages native operating system features (`nsjail` on Linux, `sandbox-exec` on macOS, and `AppContainer` on Windows) to enforce strict containment boundaries with zero startup overhead.

**Configuration**  
You can configure the sandbox behavior in your `settings.json` file (located at `~/.gemini/antigravity-cli/settings.json`):

```
{
    "enableTerminalSandbox": true
}
```

*   **`enableTerminalSandbox`** (boolean, default: `false`): Enables general execution containment barriers on all local agent processes.

**Interactive Approvals**  
When the agent proposes a terminal command that requires your confirmation, the CLI prompt adapts dynamically based on your settings:

*   **When the Sandbox is Enabled**: The confirmation prompt will include a specific option to **Yes, and run without sandbox restrictions** if you need to temporarily bypass the containment boundary for a single trusted command.
*   **When the Sandbox is Disabled**: The prompt will include an option to **Yes, and run in sandbox** if you want to force a specific, potentially risky command to execute within the safety boundary.

### CLI Slash Commands Reference

The Antigravity CLI supports a variety of slash commands typed directly into the prompt box to manage conversations, configure settings, and inspect agent capabilities.

### Core Slash Commands

| Command | Category | Purpose |
| :-- | :-- | :-- |
| **`/resume`** _(alias `/switch`)_ | Conversation | Open the conversation picker to resume or switch sessions. |
| **`/rewind`** _(alias `/undo`)_ | Conversation | Roll back conversation history to a previous checkpoint. |
| **`/rename <name>`** | Conversation | Rename the active conversation thread for easier tracking. |
| **`/permissions`** | Configuration | Select agent autonomy level (`request-review`, `always-proceed`, or `strict`). |
| **`/model`** | Configuration | Select the default reasoning model (persists across sessions). |
| **`/keybindings`** | Configuration | Open the interactive keyboard shortcut editor. |
| **`/statusline`** | Configuration | Customize real-time indicators displayed in the CLI status bar. |
| **`/tasks`** | Tools & Monitoring | Monitor, view logs for, or terminate active background tasks. |
| **`/skills`** | Tools & Monitoring | Browse local and global encapsulated agent workflows. |
| **`/mcp`** | Tools & Monitoring | Open the panel to configure and manage Model Context Protocol servers. |
| **`/open <path>`** | Utility | Immediately open a file in your preferred external editor. |
| **`/diff`** | Utility | Open the [interactive diff viewer](/docs/cli/commands/diff) to review changes and steer the agent. |
| **`/usage`** | Utility | Open the inline interactive help manual inside the terminal. |
| **`/logout`** | Account | Log out of your Google session and clear cached credentials. |

### Advanced Customization via `settings.json`

For power users, several slash commands support deep customization via your `~/.gemini/antigravity-cli/settings.json` configuration:

*   **Fine-Grained Permissions**: Instead of global levels, define specific allowed/denied commands:
    
    ```
    "permissions": {
      "allow": ["command(git)", "command(npm test)"],
      "deny": ["command(rm -rf)"]
    }
    ```
    
*   **Custom Status Line & Window Titles**: You can pipe live agent metadata (JSON format containing CWD, active model, token usage, state, etc.) directly into your own custom shell scripts to generate dynamic status bars or terminal window titles.

### Subagents in Antigravity CLI

Antigravity CLI features an asynchronous subagents framework that allows the main agent to delegate parallel work, perform background research, and run system tests without blocking your active conversation.

**What are Subagents?**  
Subagents are independent, concurrent agent sessions designed to tackle specific background tasks in parallel with the main conversation.

*   **Purpose**: The main agent automatically spawns subagents to perform background operations such as looking up documentation, running builds, or validating a fix.
*   **Capabilities**: Subagents have full access to tools such as code search, file editing, terminal commands, and web searches to complete their assigned tasks.
    *   The main agent decides what tools and permissions subagents get, including whether they can use MCP tools and if they can write files.

### Managing Agents: The `/agents` Panel

Antigravity CLI provides an interactive terminal UI to view, manage, and approve actions for running subagents.

*   **Access**: Type `/agents` in the prompt to open the subagents panel.
*   **Overview**: The panel shows a list of active and completed subagents, including surface-level details such as their status (running, done, killed, etc.) and the current step they are executing.

Note

Selecting a subagent from the panel opens a full-screen detail view. This view shows the entirety of the subagent’s conversation, including its steps, thoughts, and tool execution logs.

**Tool Confirmations & Approvals**  
When a subagent wants to execute a tool that requires user permissions (such as running a local command or writing a file), it will surface the request. You can manage approvals in two ways:

1.  **Detail View Approvals**  
    The Subagent Detail View features an interaction section containing all pending approvals, where you can selectively approve or deny requests.

> **Note**: Tip**: Use the keyboard shortcut `ctrl+j` to “teleport” from the main conversation directly to the detailed view of the next subagent waiting for your approval.

2.  **Fast Path Alerts**  
    To keep you in your flow, Antigravity CLI displays a Fast Path Alert directly above your prompt box when a subagent requests permission.

> **Note**: Tip**: You can approve a pending subagent permission instantly using `ctrl+k` without ever having to switch away from the main conversation.# Migrating from Gemini CLI

Convert your legacy configurations, import Gemini CLI extensions as native plugins, adapt custom skills paths, and reformat Model Context Protocol configurations.

## Overview

Antigravity CLI preserves backward compatibility with the core developer-experience constructs popularized by Gemini CLI. To ensure a seamless upgrade, the CLI offers automatic onboarding conversion alongside explicit CLI migration command sequences.

## First-launch onboarding

When you execute `agy` for the first time in an environment containing legacy configurations, the CLI automatically detects your existing profiles. An interactive checklist prompts you to choose which assets to migrate:

1.  **Auto-conversion**: Select the extensions and global configurations you wish to convert.
2.  **Keyring storage**: The CLI migrates your active session tokens securely into your operating system’s native keyring storage.
3.  **Settings alignment**: Default visual parameters and rendering buffers map automatically to your new settings profile.

> **Note**: Partial Parity**: While we preserve support for workspace skills, rules, and MCP servers, certain customized terminal themes or experimental visual overlays from Gemini CLI may not be supported.

## Converting extensions to plugins

Since Gemini CLI launched, the industry has standardized on the term **plugins**. You can manually convert your legacy Gemini extensions to native Antigravity plugins by executing:

```
agy plugin import gemini
```

This utility searches your legacy local directories, parses your extension manifests, and converts files into native layout blocks.

### Expected import output

```
[ok]   conductor-tools
       - skills     : skipped (none detected)
       - agents     : skipped (none detected)
       ✔ commands   : 4 legacy commands converted to skills
       - mcpServers : skipped (none detected)
[ok]   google-workspace
       ✔ skills     : 5 skills processed
       - agents     : skipped (none detected)
       ✔ commands   : 2 legacy commands converted to skills
       ✔ mcpServers : 1 server definition migrated to mcp_config.json
```

## Context files and workspace rules

Both CLI platforms utilize identical workspace context rules. No modifications are needed to your existing rule documents:

*   **Workspace local context**: The agent continues to parse and enforce rule constraints defined inside your active directory’s `GEMINI.md` and `AGENTS.md` files.
*   **Global developer context**: The agent automatically consults and enforces your global constraints located at `~/.gemini/GEMINI.md`.

## Updated skills paths

While global shared skills remain in your user home directory, the target folder path for local workspace-specific skills has been updated.

| Configuration | Gemini CLI | Antigravity CLI |
| :-- | :-- | :-- |
| **Global shared path** | `~/.gemini/skills/` | `~/.gemini/antigravity-cli/skills/` |
| **Workspace project path** | `.gemini/skills/` | `.agents/skills/` |

> **Note**: Action Required**: If your project contains custom workspace skills defined in `.gemini/skills/`, you must manually rename or relocate the folder to `.agents/skills/` for the Antigravity agent to recognize them as active slash commands.

## MCP config formatting changes

Antigravity CLI separates Model Context Protocol servers into dedicated, lightweight JSON profiles instead of nesting them inside your primary preferences configuration.

### Directory mapping

*   **Legacy Gemini Config**: Servers were declared inline within `~/.gemini/settings.json`.
*   **Antigravity CLI Config**: Servers are defined inside a standalone `mcp_config.json` profile:
    *   Global servers: `~/.gemini/config/mcp_config.json`
    *   Workspace servers: `.agents/mcp_config.json`

### Required schema updates

When manually migrating remote websocket or SSE server definitions, update the URI key parameter to match the current standard:

*   **Legacy schema keys**: `url` or `httpUrl`
*   **Modern schema key**: `serverUrl`

```
{
    "mcpServers": {
        "remote-indexer": {
            "serverUrl": "https://mcp.internal.enterprise.com/sse",
            "env": {
                "AUTH_TOKEN": "secure_alpha_token"
            }
        }
    }
}
```

## Next steps

Begin configuring your new visual parameters and troubleshooting any setup anomalies:

*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Customize keyboard hotkeys, themes, and screen buffers.
*   **[Troubleshooting](/docs/cli/troubleshooting)**: Learn how to resolve authentication lockouts or path issues.
*   **[CLI Reference](/docs/cli/reference)**: Access standard parameters lists and slash command mappings.

# Prompting & interaction

Master primary interaction patterns, multiline composition workflows, session interruption controls, and terminal media pasting.

## The prompt box

Antigravity CLI features a sticky prompt panel positioned at the bottom of your terminal screen. This panel handles standard user entries, multiline scripts, and direct media pasting.

```
───────────────────────────────────────────────────────────────────────────
> Describe your next engineering task here...
───────────────────────────────────────────────────────────────────────────
```

### Submitting prompts

To initiate an agent turn, type your instruction into the prompt panel and press `Enter`. The agent immediately analyzes your current directory workspace, reads required configurations, and begins formulating an execution plan.

### Interrupting active sessions

If the agent initiates an undesired task or loops during command execution, press `Esc` to immediately halt the session.

> **Note**: Universal Escape**: The `Esc` key acts as a global escape hatch. Pressing `Esc` instantly cancels any active agent turn, closes overlay panels, and returns focus to a clean prompt box.

## Multiline composition

For complex directives, structured test scenarios, or multi-paragraph instructions, use our built-in multiline features.

### Shorthand newline insertions

*   **Standard**: Press `Shift+Enter` or `ctrl+j` to insert a clean newline within your active prompt window without submitting.
*   **macOS Terminal Fallback**: If using Apple Terminal (which does not forward `Shift+Enter` by default), press `Option+Enter`. Ensure you check **Use Option as Meta key** in your Terminal Preferences profile.
*   **Universal Slash Escape**: Type a trailing backslash `\` at the end of your active line and press `Enter`. The CLI automatically removes the backslash and inserts a newline.

### Editing prompts in `$EDITOR`

To draft or edit extensive prompt structures in your primary development editor:

1.  Press `ctrl+g` inside the empty prompt panel.
2.  The CLI launches your system’s default text editor (such as `vim`, `nano`, or `code`, configured via `/config` or your environment’s `$EDITOR` variable).
3.  Draft your multi-line instruction inside the temporary editor buffer.
4.  Save and exit the editor. The CLI automatically imports the edited buffer directly back into the terminal prompt.

## Attaching media

Antigravity CLI supports pasting rich media formats directly from your system clipboard. Press `ctrl+v` (or native terminal paste) inside the prompt panel to attach screenshot mockups or video recordings.

### Supported file types

*   **Images**: PNG, JPEG, GIF, WebP, BMP, TIFF, and SVG.
*   **Videos**: MP4, MOV, WebM, and AVI.

## Next steps

After mastering interaction patterns, explore how the agent presents actions and requests verification:

*   **[Reviewing Artifacts](/docs/cli/artifacts)**: Learn to inspect and manage file edits, plans, and test executions.
*   **[Managing Conversations](/docs/cli/conversations)**: Resume prior threads and fork active sessions.
*   **[Background Tasks & Subagents](/docs/cli/subagents)**: Monitor asynchronous background agents.

# Reviewing artifacts

Audit generated code, review implementation proposals, attach line-level feedback comments, and verify visual media assets before applying edits to your local filesystem.

## Collaboration and co-steering

An **Artifact** is a structured deliverable created by the agent to accomplish its task and communicate its progress and thinking to you. Artifacts include rich markdown outlines (such as Implementation Plans), code diffs, architecture diagrams, and visual media files.

As agents work with higher autonomy over longer periods, artifacts enable asynchronous collaboration. You do not need to carefully monitor every individual tool execution synchronously. Instead, you review high-level deliverables at key milestones.

Because autonomous agents can occasionally go off-course or hallucinate solutions, the artifact workflow serves as a critical interactive co-steering mechanism. Depending on your configuration, the agent will pause at intermediate milestones, allowing you to inspect proposed plans or code edits, provide inline comments, and redirect the agent before any changes are physically written to your local filesystem.

The TUI partitions these assets into two interactive layers:

*   **The Artifact Picker Overlay**: A high-level checklist menu containing review status markers, quick preview toggles, and collapsible folders.
*   **The Artifact Detail Viewer**: A full-screen code audit interface supporting inline commenting, syntax highlighting, and diagram scaling.

## Overview of /artifact

When the agent produces or modifies files, a notification updates in your TUI status bar (`/artifact to review`). Press `ctrl+r` inside the prompt box to open the full-screen **Artifact Picker Panel**.

```
                                                                                                    10 artifacts · /artifact to review
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
>
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Action required (10 left)
› [ ] new release_notes.md   open  approve reject
  utils.py
  [ ] new performance_report.md
  api_client.py
  config_manager.py
  [ ] new user_guide.md
  run_tests.py
  data_processor.py
  [ ] new system_architecture.md
  [ ] new project_overview.md

Keyboard: ↑/↓ Navigate  y/n Approve/reject  shift+a Approve all  p Preview  esc Done
```

### Interaction keybindings

Audit the file checklist using the following dedicated panel controls:

| Key | TUI Command | Action Behavior |
| :-- | :-- | :-- |
| **`↑`** / **`↓`** | `nav.scroll_line` | Scrolls highlighted selections up and down through the list of entries. |
| **`h`** / **`l`** | `nav.switch_button` | Focuses and toggles between inline row buttons: **open**, **approve**, and **reject** (Left/Right arrows also supported). |
| **`p`** | `confirm.preview` | Toggles a **quick inline file preview**. This opens a 12-line truncated and indented code block preview directly under the selected row. |
| **`y`** | `confirm.approve` | Instantly approves the highlighted file. The status marker updates to a green checkmark (`✓ approved`). |
| **`n`** | `confirm.reject` | Instantly rejects the highlighted file. The status marker updates to a red cross (`✗ rejected`). |
| **`Shift+A`** | `confirm.approve_all` | Bulk-approves all pending actionable files in one action. |
| **`Shift+R`** | `confirm.reject_all` | Bulk-rejects all pending actionable files in one action. |
| **`Enter`** | `nav.confirm` | Executes the active focused button. If the `open` button is focused, it launches the full-screen Detail Viewer. |
| **`Esc`** | `nav.escape` | Saves your active review state, submits approvals/rejections back to the agent thread, and returns focus to the prompt box. |

### Code files vs visual media

To organize workspace assets, the picker separates files by format types:

*   **Actionable Code Files**: Standard programming codes, configs, and plan markdowns that require explicit approvals.
*   **Collapsible Media Drawer**: Visual asset files (such as PNG, JPG, WebP, SVG, MP4, or WebM media) are grouped into a dedicated **“Media”** drawer header.
    *   Highlight the **Media** header row and press `Enter` to expand or collapse the drawer list.
    *   Highlight a specific media item and press `Enter` to open the file inside your operating system’s native media viewer.

* * *

## Viewing an artifact

To launch a close audit of a file’s code structure or proposed logic, select `open` (or press `Enter` directly on a highlighted code row) to open the **Artifact Detail Viewer**.

```
implementation_plan.md
>   1      Implementation Plan: Alpha-Centauri Telemetry Scaling Engine
    2
    3     This document provides a highly detailed, step-by-step engineering implementation plan to upgrade the Alpha-Centauri
    4     telemetry ingestion pipeline. It outlines current gaps, proposed architecture improvements, execution timelines, risks,
    5     and verification procedures.
    6     ──────
    7     ## 1. Executive Summary
    8
    9     As sensor deployments scale from 100 to 10,000 active nodes, the existing synchronous Python-based ingestion system (
   10     data_processor.py ) faces critical CPU and write latency bottlenecks.
   11
   12     This implementation plan details the migration to an asynchronous, remote-buffered pipeline utilizing distributed
   13     message
   14     queues, multi-threaded worker pools, and an optimized column-oriented storage layer.
   15     ──────
   16     ## 2. Current Architecture vs. Target Architecture
   17
   18     ### Gap Analysis
   19
   20      Feature    | Existing (v1.2)   | Target (v2.0)     | Gap to Resolve
   21     ------------|-------------------|-------------------|---------------------------
   22      Concurrency| Sync, 1-thread    | Async, concurrent | Cannot scale peak bursts
   23      Buffer     | None (direct API) | Message Queue     | Outage data loss
   24      Storage    | Flat JSON         | Columnar CNS      | Slow queries, high consumption
   25      Config     | Load on launch    | Dynamic polling   | Requires restarts to update
   26
   27     ### Architectural Schema
   28
   29         Ingestion Layer │ Buffering Layer │ Processing Layer │ Storage Layer
   30
   31         ┌────────────┐    ┌────────────┐
   32         │ "Sensor 1" │    │ "Sensor 2" │
   33         └────────────┘    └────────────┘
   34                │ HTTP POST           │ HTTP POST
   35                ▼                 ▼
   36         ┌─────────────────┐
   37         │ "Load Balancer" │
   38         └─────────────────┘
   39                  │
   40                  ▼
   41         ┌───────────────────────┐    ┌───────────────────────┐
   42         │ "Ingestion Gateway A" │    │ "Ingestion Gateway B" │
   43         └───────────────────────┘    └───────────────────────┘
   44                     │ Publish                    │ Publish
   45                     ▼                            ▼
   46         ┌─────────────────────────────┐
   47         │ "Distributed Message Queue" │
   48         └─────────────────────────────┘
   49                        │ Stream Consume
   50                        ▼
   51         ┌────────────────────┐    ┌────────────────────┐
   52         │ "Worker Process 1" │    │ "Worker Process 2" │
   53         └────────────────────┘    └────────────────────┘
   54                    │ Read Config               │ Read Config
   55                    ▼                         ▼
   56         ┌──────────────────────────┐    ┌──────────────────────────┐
   57         │ "Dynamic Config Service" │    │ "Columnar Storage (CNS)" │
  [0%  L1  1-57/135]

  ↑/↓ scroll · pgup/pgdown page · shift+g bottom · g top · c comment · m raw mermaid · ctrl+=/ctrl+- zoom 100%
  l hide lines · esc close
```

### Auditing & navigation

*   **Scrolling**: Scroll page-by-page or line-by-line using `j`/`k` (or standard arrow keys).
*   **Boundary Jump**: Press `g` to jump to the top of the file, and `Shift+G` to jump directly to the bottom.
*   **Toggle Gutter**: Press `l` to toggle the line number gutter on and off for a cleaner presentation of the raw code.

### Granular line commenting

If a specific block of code requires correction:

1.  Navigate and position your cursor on the target line.
2.  Press `c` to open an inline, multi-line text editor buffer attached directly to that line.
3.  Draft your descriptive feedback, and press `Esc` to save and submit the comment. The line is updated with a visual comment indicator (`💬`).
4.  To delete your active feedback, position your cursor on the commented line and press `d`.

### Custom Mermaid diagram rendering

If the active document contains structured system flowcharts, database relationships, or architectural layouts:

*   **Cycle Render Modes (`m`)**: Press `m` to cycle visual rendering modes:
    *   **Kitty Graphics Image**: Renders diagrams natively as inline graphics within Kitty-compatible terminal emulators.
    *   **ASCII Box Art** (Default): Renders diagrams as clean, high-performance text art compatible with all shells.
    *   **Raw Code**: Shows the raw markdown code block fences.
*   **Zooming Graphics**: When Kitty graphics image mode is active, press `ctrl+=` to zoom in and scale up the image, and `ctrl+-` to zoom out.

Press `Esc` to close the Detail Viewer and return back to the primary picker checklist.

## Next steps

Configure settings preferences and review agent autonomy parameters:

*   **[Managing Conversations](/docs/cli/conversations)**: Resume prior sessions and fork branches.
*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Customize keyboard hotkeys and visual buffers.
*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Configure security parameters and containment lists.

# Managing conversations

Resume prior development threads, scope active histories to local workspaces, and fork conversations to experiment with alternate architectures.

## Workspace scoping

To maintain context hygiene, Antigravity CLI scopes conversation histories directly to your current working directory. When you launch `agy` from a specific directory, the agent only displays and resume sessions associated with that specific local repository or subdirectory.

This prevents context pollution, ensuring that the agent’s semantic memory and token limits remain focused solely on the relevant codebase.

## Resuming sessions

You can return to a prior conversation at any time to continue an implementation, refine a solution, or recover from an interrupted session.

Antigravity CLI supports both an interactive **Session Picker** TUI overlay and direct command-line flags (`agy -c` / `agy --continue`) to resume threads instantly based on your active workspace.

For a complete walkthrough of the interactive picker, keyboard shortcuts, and details on how the directory-scoped session cache works, see the dedicated **[Resume Command Guide](/docs/cli/commands/resume)**.

## Branching with `/fork`

When engineering a complex feature, you may want to explore multiple design alternatives without losing your progress. The `/fork` command enables safe, parallel experimentation.

```
/fork
```

_(Alias: `/branch`)_

The `/fork` command clones your entire conversation history up to the current turn into a new, independent session.

### Forking workflow

1.  Type `/fork` inside the prompt panel and press `Enter`.
2.  The CLI allocates a new unique session ID and duplicates your existing workspace state and agent thread.
3.  Your active terminal switches immediately to the new branch.
4.  If the experiment fails, run `/resume` to restore your original, stable conversation branch.

> **Note**: Branching Filesystems**: Forking clones the _conversation thread_, not your local git checkout. To fully isolate files during parallel forks, use git branches or stash local changes before testing contrasting approaches.

## Next steps

Explore how the agent handles complex, asynchronous operations and parallel tasks:

*   **[Background Tasks & Subagents](/docs/cli/subagents)**: Monitor subagents and handle fast-path approvals.
*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Configure rendering buffers and override JSON preferences.
*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Manage security profiles and system command lists.

# Choose an execution mode

Control whether Antigravity CLI pauses to ask before modifying files or executing commands during a session.

## Before you begin

*   [Install Antigravity CLI](/docs/cli/install)
*   Have an active project repository with source code to edit

## Available modes

Each execution mode makes a different tradeoff between conversational autonomy and developer oversight. The table below shows how Antigravity CLI handles file operations and planning in each mode.

| Mode | Behavior | Best for |
| :-- | :-- | :-- |
| `default` | Pauses for interactive diff review before modifying or creating files. | Standard development, reviewing sensitive code changes, and careful refactoring. |
| `accept-edits` | Automatically approves file edits and creations (`mkdir`, `touch`, file writes). | Rapid prototyping, iterating on trusted code, and reducing prompt interruptions. |
| `plan` | Prepends the `/plan` instruction prefix to analyze and outline steps before writing code. | Exploring unfamiliar architecture or designing complex multi-step features. |

> **Note:** Tool permission rules configured via `/permissions` or `--dangerously-skip-permissions` continue to govern shell commands (`run_command`) across all execution modes.

## Cycle execution modes during a session

You can switch execution modes mid-session without interrupting active tasks or restarting the terminal.

1.  Press `Shift+Tab` inside the prompt box to cycle through the active sequence: `default` → `accept-edits` → `plan` → `default`
    
2.  Observe the status bar indicator below the prompt input to confirm your active mode (`[accept-edits]` or `[plan]`).
    

> **Tip:** When Antigravity CLI pauses for a pending file edit confirmation in `default` mode, you can press `Shift+Tab` to instantly switch to `accept-edits` mode and approve all pending file modifications.

## Review modifications in default mode

In `default` mode (`request-review`), Antigravity CLI pauses before applying any file writes to disk and renders an inline, syntax-highlighted diff preview.

```
# Launch in default interactive review mode
agy
```

When prompted with a pending file modification:

*   Press `y` to accept the changes and save the file to disk.
*   Press `n` to reject the edits and keep the existing file unchanged.
*   Press `f` (`KeyViewDiff`) to open a full-screen, scrollable diff review with 3 context lines and hunk separators.
*   Press `Ctrl+G` to open the file inside your `$EDITOR` for manual adjustments.
*   Type instructions in the prompt box and press `Enter` to reject the edit and tell the agent what to do differently.

![The default mode file edit diff review panel showing line modifications and action choices](/assets/image/docs/cli/modes-edit-file-preview.png)

### New file creation previews

When Antigravity CLI creates a brand-new file, the confirmation panel displays an addition-only diff preview with a dedicated `"Create file"` header and explicit allow/deny prompts:

```
Create file: src/utils/formatter.ts
Allow create this file? [y/n/f]
```

![The addition-only diff confirmation panel displayed when creating a new file in default mode](/assets/image/docs/cli/modes-create-file-preview.png)

## Auto-approve edits with accept-edits mode

Select `accept-edits` mode when you want Antigravity CLI to work in longer, uninterrupted stretches across your filesystem without pausing for each file modification.

```
# Launch directly in accept-edits mode
agy --mode=accept-edits
```

In this mode, all standard file read, creation, and replacement operations (`write_to_file`, `replace_file_content`, `multi_replace_file_content`) run automatically. Subagents spawned during the session also inherit the `accept-edits` setting, preventing background file writes from queueing for manual approval.

![The CLI running in accept-edits mode showing the status indicator and automatic file modification](/assets/image/docs/cli/modes-accept-edits-status.png)

## Analyze tasks before editing with plan mode

Use `plan` mode when taking on complex refactoring, multi-file architectural changes, or unfamiliar codebase investigations.

```
# Launch directly in planning mode
agy --mode=plan
```

When `plan` mode is active via `Shift+Tab` cycling or the `--mode` flag, the CLI automatically prepends the `/plan` instruction prefix to your prompts. The agent investigates relevant files using read-only tools (`code_search`, `grep_search`, `view_file`) and presents a structured execution outline for your approval before writing code.

![The CLI running in plan mode analyzing code and structuring an execution outline](/assets/image/docs/cli/modes-plan-execution.png)

## Persist or override your default mode

You can set your preferred startup execution mode permanently across sessions or override it for specific invocations.

### Using the interactive settings panel

Open the interactive settings panel mid-session to inspect or update your default configuration.

```
/settings
```

![The interactive settings panel with the Agent Mode option highlighted](/assets/image/docs/cli/modes-settings-panel.png)

Navigate to **Agent Mode** using `↑`/`↓`, press `Enter` or `Space` to select your default (`default`, `accept-edits`, or `plan`), and press `Ctrl+S` to save. Modifying this option synchronizes your runtime `CycleMode` immediately.

### Setting `agentMode` in `settings.json`

Set `agentMode` directly inside your user or project configuration file:

```
{
    "agentMode": "accept-edits"
}
```

The CLI loads this file from `~/.gemini/antigravity-cli/settings.json` at startup and applies your chosen baseline execution mode.

### Command-line flag overrides

Pass the `--mode` flag to temporarily override your persistent default mode for a single terminal run:

```
# Override settings.json to run in planning mode
agy --mode=plan
```

## Common mistakes

| Mistake | Why it fails | Fix |
| :-- | :-- | :-- |
| Expecting `sandbox` in `Shift+Tab` cycling | `sandbox` is an OS containment permission setting, not an execution mode | Configure sandbox auto-approval rules inside `/permissions` |
| Using legacy `/planning` or `/fast` commands | These vestigial commands were removed in `1.1.0` | Press `Shift+Tab` to cycle modes or type `/plan` before your prompt |
| Passing `--permission-mode` | `agy` uses `--mode` (`--mode=accept-edits` or `--mode=plan`) for execution overrides | Run `agy --mode=accept-edits` or check `agy --help` |

## Next steps

*   [Permissions](/docs/cli/permissions): Configure fine-grained tool approval rules and wildcard matching
*   [Settings, Rendering & Keybindings](/docs/cli/settings): Customize configuration overrides and interactive preferences
*   [Background Tasks & Subagents](/docs/cli/subagents): Manage parallel subagent execution and asynchronous task queues

# Headless mode

Run Antigravity CLI non-interactively to script agent tasks, integrate with CI pipelines, and capture machine-readable output.

Headless mode (also called print mode) sends a single prompt to the agent, streams or returns the response, and exits. Use it whenever you need the agent’s output in a program instead of a terminal UI.

## Run a single prompt

Pass a prompt with `-p` (or its aliases `--print` and `--prompt`) to run once and exit:

```
agy -p "In one sentence, what is a git rebase?"
```

```
A git rebase rewrites the commit history by transplanting a sequence of commits onto a new base commit, imposing a strictly linear progression of changes that eliminates arbitrary merge artifacts.
```

The response goes to `stdout`. Diagnostics — errors, authentication prompts, progress, and permission notices — go to `stderr`. This split keeps the captured response clean:

```
# Capture only the model response; diagnostics still print to the terminal.
answer=$(agy -p "Name three popular version control systems, comma-separated.")
```

> **Note:** Headless mode uses your cached credentials. Authenticate once with an interactive `agy` session first. In a non-interactive environment with no terminal (for example, CI), a run that is not already authenticated exits with an `authentication required` error instead of hanging.

## Output formats

The `--output-format` flag controls the shape of `stdout`. It accepts three values:

| Format | `stdout` shape | Use it for |
| --- | --- | --- |
| `text` | The response text (default) | Human-readable output, quick scripts |
| `json` | One JSON object printed on completion | Capturing a result plus metadata |
| `stream-json` | Newline-delimited JSON (NDJSON) events | Monitoring progress, tools, and token usage |

### Text

The default. The response text goes straight to `stdout` with no wrapping:

```
agy -p "In one sentence, what does the command git bisect do?"
```

```
Git bisect executes a binary search algorithm across a project's commit history to rapidly isolate the precise commit responsible for introducing a defect.
```

### JSON

Set `--output-format json` to get a single JSON envelope after the run completes. The CLI emits it on one line; pipe through `jq` to pretty-print:

```
agy -p "In one sentence, what is a git rebase?" --output-format json | jq
```

```
{
  "conversation_id": "055a398f-db14-4c5f-abbb-1bf03f8120a7",
  "status": "SUCCESS",
  "response": "A git rebase rewrites the commit history by transplanting a sequence of commits onto a new base commit, imposing a strictly linear progression of changes that eliminates arbitrary merge artifacts.\n",
  "duration_seconds": 7.16,
  "num_turns": 1,
  "usage": {
    "input_tokens": 10415,
    "output_tokens": 657,
    "thinking_tokens": 616,
    "cache_read_tokens": 8113,
    "total_tokens": 11072
  }
}
```

The envelope contains these fields:

| Field | Type | Description |
| --- | --- | --- |
| `conversation_id` | string | ID of the conversation, for resuming later |
| `status` | string | Terminal status (see [Status values](#status-values)) |
| `response` | string | The agent’s free-text response |
| `error` | string | Error message; present only on failure |
| `duration_seconds` | number | Wall-clock duration of the run |
| `num_turns` | number | Number of user turns in the conversation |
| `structured_output` | object | Parsed schema output; present only with `--json-schema` |
| `json_schema` | object | The schema that was enforced; present only with `--json-schema` |
| `usage` | object | Token counts: `input_tokens`, `output_tokens`, `thinking_tokens`, `cache_read_tokens`, `total_tokens` |

#### Structured output with a schema

Pass `--json-schema` to constrain the answer to a schema. The parsed object appears in `structured_output`, and `response` holds the same payload serialized as a string:

```
agy -p "Parse the semantic version string v2.14.3 into an object with integer fields major, minor, and patch." \
  --output-format json \
  --json-schema '{"type":"object","properties":{"major":{"type":"integer"},"minor":{"type":"integer"},"patch":{"type":"integer"}},"required":["major","minor","patch"]}' | jq
```

```
{
  "conversation_id": "4e502687-290c-4030-b908-5ed6c68fa5dc",
  "status": "SUCCESS",
  "response": "{\"major\":2,\"minor\":14,\"patch\":3}\n",
  "duration_seconds": 4.45,
  "num_turns": 1,
  "structured_output": { "major": 2, "minor": 14, "patch": 3 },
  "json_schema": {
    "type": "object",
    "properties": {
      "major": { "type": "integer" },
      "minor": { "type": "integer" },
      "patch": { "type": "integer" }
    },
    "required": ["major", "minor", "patch"]
  },
  "usage": { "input_tokens": 10522, "output_tokens": 354, "thinking_tokens": 329, "cache_read_tokens": 8112, "total_tokens": 10876 }
}
```

The flag accepts a schema string, a path to a `.json` schema file, or a primitive type name (`string`, `number`, `integer`, `boolean`). Read the parsed value from `structured_output`:

```
agy -p "Parse the semantic version string v2.14.3 into an object with integer fields major, minor, and patch." \
  --output-format json \
  --json-schema '{"type":"object","properties":{"major":{"type":"integer"},"minor":{"type":"integer"},"patch":{"type":"integer"}},"required":["major","minor","patch"]}' \
  | jq '.structured_output'
```

### Streaming JSON

Set `--output-format stream-json` to emit one JSON object per line (NDJSON) as the run progresses. Use this format to observe tool calls and token usage in real time.

```
agy -p "In one sentence, what is a git rebase?" --output-format stream-json
```

The stream begins with one `init` event, followed by any number of `step_update` events, and ends with exactly one `result` event (the `cwd` and `tools` array are abbreviated below):

```
{"event":"init","conversation_id":"c3b66b04-872b-4fbe-a3a4-058a026ef20a","init":{"cwd":"/home/user/project","tools":["ask_permission","run_command","write_to_file","..."],"permission_mode":"request-review"}}
{"event":"step_update","step_update":{"conversation_id":"c3b66b04-872b-4fbe-a3a4-058a026ef20a","step_index":0,"state":"DONE","step_type":"user_input"}}
{"event":"step_update","step_update":{"conversation_id":"c3b66b04-872b-4fbe-a3a4-058a026ef20a","step_index":3,"state":"DONE","step_type":"agent_response","text_delta":"Git rebase destructively rewrites a branch's commit history by systematically detaching its unique commits and sequentially reapplying them onto a new base commit.\n","duration_seconds":6.28,"usage":{"input_tokens":10302,"output_tokens":582,"thinking_tokens":551,"cache_read_tokens":8113,"total_tokens":10884}}}
{"event":"step_update","step_update":{"conversation_id":"c3b66b04-872b-4fbe-a3a4-058a026ef20a","step_index":4,"state":"DONE","step_type":"checkpoint","duration_seconds":0.53,"usage":{"input_tokens":116,"output_tokens":7,"thinking_tokens":0,"cache_read_tokens":0,"total_tokens":123}}}
{"event":"result","result":{"conversation_id":"c3b66b04-872b-4fbe-a3a4-058a026ef20a","status":"SUCCESS","response":"Git rebase destructively rewrites a branch's commit history by systematically detaching its unique commits and sequentially reapplying them onto a new base commit.\n","duration_seconds":6.88,"num_turns":1,"usage":{"input_tokens":10418,"output_tokens":589,"thinking_tokens":551,"cache_read_tokens":8113,"total_tokens":11007}}}
```

When the response streams in chunks, the `agent_response` step emits one or more `ACTIVE` events carrying partial `text_delta` fragments before its final `DONE`; short responses like this one arrive in a single `DONE`.

Every line is an event object whose `event` field names its type:

| `event` | Payload key | Emitted |
| --- | --- | --- |
| `init` | `init` | Once, at stream start |
| `step_update` | `step_update` | For each step transition or text delta |
| `result` | `result` | Once, at the end (same shape as `json`) |

The `init` payload records the run configuration. `model` and `agent` appear only when set with `--model` or `--agent`; `permission_mode` is `request-review` by default (and `always-proceed` under `--dangerously-skip-permissions`):

| Field | Type | Description |
| --- | --- | --- |
| `cwd` | string | Working directory |
| `tools` | string\[\] | Names of all available tools |
| `permission_mode` | string | Effective permission mode |
| `model` | string | Model in use, when overridden |
| `agent` | string | Active agent, when overridden |
| `json_schema` | object | Enforced schema, when set with `--json-schema` |

Each `step_update` payload describes one step. Observed `step_type` values include `user_input`, `agent_response`, `tool`, and `checkpoint`; `state` is `ACTIVE` while a step runs and `DONE` when it finishes:

| Field | Type | Description |
| --- | --- | --- |
| `conversation_id` | string | ID of the conversation |
| `step_index` | number | Zero-based index of the step |
| `state` | string | `ACTIVE` or `DONE` |
| `step_type` | string | Step category, for example `agent_response` or `tool` |
| `tool_name` | string | Canonical tool name, on tool steps |
| `text_delta` | string | Incremental response text |
| `duration_seconds` | number | Step duration, when known |
| `usage` | object | Per-step token usage, when known |
| `tool_info` | object | Tool invocation details (see below) |
| `subagent_info` | object | Subagent invocation details |

#### Tool calls in the stream

On tool steps, `tool_info` carries the call and its result. This is a real tool step from a run that executed `echo hello_headless_demo`:

```
{"event":"step_update","step_update":{"conversation_id":"edb1c8c1-50ba-4f3f-87eb-412d0e9d47c3","step_index":4,"state":"DONE","step_type":"tool","tool_name":"run_command","duration_seconds":0.07,"tool_info":{"name":"run_command","parameters":{"CommandLine":"echo hello_headless_demo"},"output":"hello_headless_demo\r\n"}}}
```

`tool_info` holds `name`, `parameters`, `output`, and — when the tool fails — an `error` object with `type` and `message`. Steps that spawn subagents carry `subagent_info` instead, listing each subagent under `subagents` (with `type_name`, `role`, `conversation_id`, `log_uri`, and `workspace_uris`).

#### Structured output in the stream

With `--json-schema`, the schema applies to the terminal `result` event, which carries the same `structured_output` and `json_schema` fields as the `json` envelope.

## Parse output with jq

`stdout` is machine-readable, so `jq` extracts exactly what you need.

Get the response text from a JSON run:

```
agy -p "Name three popular version control systems, comma-separated." --output-format json | jq -r '.response'
```

```
Git, Subversion, Mercurial.
```

Concatenate streaming text as it arrives:

```
agy -p "Explain what a merge conflict is in two sentences." --output-format stream-json \
  | jq -j 'select(.event=="step_update") | .step_update.text_delta // empty'
```

Read token usage from the terminal `result` event:

```
agy -p "In one sentence, what is a git rebase?" --output-format stream-json \
  | jq 'select(.event=="result") | .result.usage'
```

> **Tip:** Use `jq -j` (join output) when concatenating `text_delta` fragments so `jq` does not insert newlines between them.

## Continue a conversation

Headless runs are stateless by default. Resume prior context with `--continue` (`-c`) for the most recent conversation, or `--conversation` with an ID from a previous run’s `conversation_id`:

```
# Continue the most recent conversation.
agy -p "Now explain your previous answer in more detail" --continue

# Resume a specific conversation by ID.
agy -p "Summarize what we discussed" --conversation 055a398f-db14-4c5f-abbb-1bf03f8120a7
```

## Select a model, effort, or agent

List the available model slugs, then pin one for the run:

```
agy models
```

```plaintext
gemini-3.7-flash-high     Gemini 3.7 Flash (High)
gemini-3.7-flash-medium   Gemini 3.7 Flash (Medium)
gemini-3.6-flash-high     Gemini 3.6 Flash (High)
gemini-3.6-flash-medium   Gemini 3.6 Flash (Medium)
gemini-3.5-flash-medium   Gemini 3.5 Flash (Medium)
gemini-3.1-pro-high       Gemini 3.1 Pro (High)
claude-sonnet-4-6         Claude Sonnet 4.6 (Thinking)
...
```

```
# Pin a model by slug.
agy -p "Reverse the string antigravity." --model gemini-3.5-flash-medium

# Set reasoning effort (low, medium, or high).
agy -p "Outline a plan to add caching to this service." --effort high

# Select an agent (list them with `agy agents`).
agy -p "Review this function for edge cases." --agent <agent-name>
```

Unlike the interactive UI, headless mode does not silently fall back when `--model` names an unknown model. It exits non-zero with an `ERROR` status so a pinned pipeline fails loudly instead of running the wrong model.

## Permissions in headless mode

There is no interactive prompt in headless mode, so tools that would normally ask for confirmation are handled by policy.

By default, the CLI respects the permission mode in your settings. A tool that requires approval it cannot obtain is soft-denied: the run continues, exits `0`, and prints a notice to `stderr` naming the tool and how to allow it. Reading and writing files inside your active workspace is auto-allowed; actions such as shell commands default to **Ask** and are soft-denied in headless mode unless you grant them.

Grant a tool ahead of time by adding an `action(target)` rule under `permissions.allow` in `~/.gemini/antigravity-cli/settings.json`:

```
{
  "permissions": {
    "allow": ["command(git)", "command(npm run (build|lint|test))", "write_file(src/)"]
  }
}
```

To auto-approve every tool for a run, pass `--dangerously-skip-permissions`:

```
agy -p "Run the test suite and report failures" --dangerously-skip-permissions
```

> **Warning:** `--dangerously-skip-permissions` approves all tool calls, including file writes and command execution. Prefer scoped `permissions.allow` rules unless you fully trust the prompt and environment. See [Permissions](/docs/cli/permissions) for the full rule syntax.

## Handle exit codes and errors

A successful run exits `0`. A run that fails to produce a response exits non-zero and writes the reason to `stderr`. In `json` and `stream-json` modes, the failure also appears in the `status` and `error` fields.

For example, pinning an unknown model exits `1` and returns an error envelope:

```
agy -p "hi" --model does-not-exist-model --output-format json; echo "exit=$?"
```

```
{"conversation_id":"","status":"ERROR","response":"","error":"invalid model selection (--model \"does-not-exist-model\" --effort \"\"): model does-not-exist-model is not recognized as a known model or custom model in settings\nAvailable models:\n  Gemini 3.6 Flash (High)\n  ...","duration_seconds":0,"num_turns":0,"usage":{"input_tokens":0,"output_tokens":0,"thinking_tokens":0,"cache_read_tokens":0,"total_tokens":0}}
```

```
exit=1
```

The `status` field reports the terminal state of the run:

| Status | Meaning |
| --- | --- |
| `SUCCESS` | The run completed and produced a response |
| `ERROR` | The run ended with an error |
| `CANCELED` | The run was canceled |
| `INTERRUPTED` | The run was interrupted (for example, `SIGINT`) |
| `INVALID` | The run reached an invalid state |
| `WAITING` | The run ended while waiting on input |
| `RUNNING` | The run did not reach a terminal state |

By default, a run waits up to five minutes for a response. Adjust the ceiling with `--print-timeout`:

```
agy -p "Summarize the design tradeoffs of optimistic locking." --print-timeout 15m
```

## Flag reference

| Flag | Default | Description |
| --- | --- | --- |
| `-p`, `--print`, `--prompt` | — | Run a single prompt non-interactively and print the response |
| `--output-format` | `text` | Output format: `text`, `json`, or `stream-json` |
| `--json-schema` | — | Schema string or file path to enforce structured output |
| `--model` | — | Model slug for this run (see `agy models`) |
| `--effort` | — | Reasoning effort: `low`, `medium`, or `high` |
| `--agent` | — | Agent for this run (see `agy agents`) |
| `--continue`, `-c` | `false` | Continue the most recent conversation |
| `--conversation` | — | Resume a conversation by ID |
| `--dangerously-skip-permissions` | `false` | Auto-approve all tool permission requests |
| `--print-timeout` | `5m` | Maximum time to wait for a response |
| `--sandbox` | `false` | Run with terminal sandbox restrictions enabled |

## Example: run the agent in CI

Fail the job on error and save the response:

```
#!/usr/bin/env bash
set -euo pipefail

result=$(agy -p "Name three popular version control systems, comma-separated." \
  --output-format json \
  --print-timeout 10m)

status=$(echo "$result" | jq -r '.status')
if [[ "$status" != "SUCCESS" ]]; then
  echo "Agent run failed: $(echo "$result" | jq -r '.error')" >&2
  exit 1
fi

echo "$result" | jq -r '.response' > result.txt
```

## Next steps

*   [Prompting & Interaction](/docs/cli/prompting): Write effective prompts for the agent.
*   [Permissions](/docs/cli/permissions): Configure allow, deny, and ask rules.
*   [Background Tasks & Subagents](/docs/cli/subagents): Delegate work to specialized agents.
*   [Reference](/docs/cli/reference): Full command and flag reference.

# Background tasks & subagents

Delegate slow builds, multi-file code generation, and research sweeps to parallel background agents while maintaining your active programming flow.

> **Note**: Antigravity 2.0 & Hub Docs:** For core platform capabilities, subagent lifecycle state diagrams, inter-agent messaging, and nesting depth limits, see the [Antigravity 2.0 Subagents Documentation](/docs/subagents).

## Asynchronous execution model

To maximize developer velocity, Antigravity CLI leverages a multi-threaded asynchronous execution architecture. Instead of locking your terminal session during long-running builds, massive codebase search sweeps, or complex multi-file edits, the primary agent delegates these operations to parallel **Subagents** or background **Tasks**.

This delegation model ensures you never have to wait on high-latency AI processes. You can continue drafting code, submitting prompts, or inspecting files while multiple autonomous background threads execute validation tasks in parallel.

## Managing agents: The `/agents` panel

The active agent-hierarchy and custom agent selection menu are fully transparent and manageable through the interactive [Agent Manager Panel (`/agents`)](/docs/cli/commands/agents).

### Opening the panel

Type `/agents` in the prompt and press Enter to open the interactive **Agent Manager Panel**.

### Panel overview

The panel displays a live checklist of all active, completed, killed, or failed background agents:

*   **Identifier**: The unique target subagent ID.
*   **Role**: The specialized role of the agent (such as “Codebase Researcher” or “Database Debugger”).
*   **State**: Live status indicators (running, done, killed, or error).
*   **Step**: A real-time summary of the tool or reasoning step currently being executed.

Tip

You can also select and switch between custom agents (or fork conversations) from this panel. See the [`/agents` command reference](/docs/cli/commands/agents) for full details on custom agent discovery and panel keybindings.

## Custom Agents (Markdown Format)

In addition to built-in agents, the CLI automatically discovers custom agents defined in Markdown format (`.md`) with YAML frontmatter:

*   **Workspace Agents**: `.agents/agents/<name>.md` or `.agents/agents/<name>/agent.md`
*   **Global Agents**: `~/.gemini/config/agents/`

When a custom agent has `subagent: true` set in its YAML frontmatter, the primary agent can invoke it via `invoke_subagent`. You can also select custom agents directly as your primary agent in the `/agents` panel menu.

For the complete schema, frontmatter parameters, and code examples, see [Custom Subagents Specification](/docs/subagents#custom-subagents).

## Deep-dive monitoring

To inspect the inner reasoning, thoughts, and logs of a specific background agent:

1.  Open the `/agents` panel and highlight the target agent using ↑/↓.
2.  Press Enter to open the **Subagent Detail View**.
3.  Inspect the subagent’s entire reasoning log, including its private internal thoughts, tool calls, and execution outputs.
4.  Press Esc to exit and return to the main Agent Manager list.

## Monitoring background tasks with `/tasks`

For non-agentic background operations, such as direct shell commands, testing suites, or simple background queries initiated via `/btw`, use the `/tasks` command.

```
/tasks
```

The tasks tracking list lets you:

*   Track standard non-interactive background processes.
*   Select a task using ↑/↓ and press Enter to view stdout logs.
*   Terminate runaway terminal processes safely.

## Keyboard ergonomics

To reduce context-switching friction when subagents require manual interaction or tool authorizations, Antigravity CLI integrates high-efficiency shortcut paths.

### Detailed “Teleport” navigation (`Alt+J`)

When a subagent encounters a tool requiring approval (e.g. writing a file or running a database migration), a status bar notification blinks.

*   Press Alt + J inside the main prompt panel to instantly “teleport” from your current conversation directly into the Detail View of the next subagent awaiting your approval.
*   Confirm or reject the action, and press Esc to teleport back to your primary thread.

### ”Fast-Path” confirmations (`Ctrl+K`)

To authorize an agent action instantly without leaving your active workspace:

1.  Look at the inline status notification displayed right above your active prompt box. It summarizes the pending action (e.g., `Subagent 12 asks to run "npm test"`).
2.  Press Ctrl + K to instantly approve the pending fast-path action without switching panels or opening overlays.

## Next steps

Configure the visual shell behavior and customize your configuration profiles:

*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Customize key maps, buffering, and JSON rules.
*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Enforce security containment rings on background processes.
*   **[Plugins & Skills](/docs/cli/plugins)**: Create your own custom skills and slash commands.

# Sandbox

Enforce native operating system process isolation, manage execution containment boundaries, and protect your local workstation.

## The security model

Because autonomous development agents run local terminal commands, edit source codes, and execute tests directly in your workspace, maintaining a secure workstation environment is critical. Antigravity CLI integrates a native **Terminal Sandbox** to restrict destructive shell operations or unauthorized remote network calls.

### Native OS containment

Unlike heavy virtual containers or isolated virtual machines that slow down execution speeds, Antigravity uses lightweight, native operating system kernel utilities to create secure process rings with zero execution overhead:

| Operating System | Sandboxing Utility | Security Characteristics |
| :-- | :-- | :-- |
| **Linux** | `nsjail` | Open-source process isolator utilizing kernel namespaces and cgroups to confine CPU, memory, and path visibility. |
| **macOS** | `sandbox-exec` | Native system tool enforcing policy profiles that restrict absolute filesystem access and raw TCP queries. |
| **Windows** | `AppContainer` | Desktop security containment ring isolating filesystem permissions and registry visibility. |

## Activating the sandbox

You configure the sandbox directly inside your global preferences:

```
~/.gemini/antigravity-cli/settings.json
```

### Sandbox configurations

Add the sandboxing toggle to your settings profile:

```
{
    "enableTerminalSandbox": true
}
```

*   **`enableTerminalSandbox`** (boolean, default: `false`): Restricts all local execution commands launched by agents to OS containment rings.

## Interactive approvals with sandbox

When the agent attempts to run a terminal tool or shell command, the TUI prompt block adapts dynamically based on your sandboxing state:

*   **When Sandbox is Enabled**: The prompt panel offers a temporary escape option:
    
    ```
    Do you want to proceed?
    1. Yes
    2. Yes, and run without sandbox restrictions
    3. No
    ```
    
    Choosing Option 2 bypasses the containment barrier exclusively for that single execution run.
*   **When Sandbox is Disabled**: The prompt lets you force containment for a risky command:
    
    ```
    Do you want to proceed?
    1. Yes
    2. Yes, and run in sandbox
    3. No
    ```
    

## See also

*   **[Permissions Engine](/docs/cli/permissions)**: Configure fine-grained allow/deny policy rules.
*   **[Plugins & Skills](/docs/cli/plugins)**: Create your own custom skills slash commands.
*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Customize keyboard hotkeys and buffers.

# Permissions

Secure your local workstation, restrict absolute file paths, configure custom allow/deny/ask policies, and manage interactive approvals. You can also manage these rules interactively using the **[Permissions Command](/docs/cli/commands/permissions)**.

## Fine-grained permissions

To secure your workstation while enabling autonomous workflows, Antigravity CLI integrates a robust **Fine-Grained Permissions Engine**. Every sensitive operation the agent performs is represented as a **permission resource** formatted as `action(target)`.

Permissions are evaluated across three distinct access lists configured inside your global settings:

```
~/.gemini/antigravity-cli/settings.json
```

*   **`deny`**: The action is blocked immediately.
*   **`ask`**: The agent pauses and prompts for your explicit approval before proceeding.
*   **`allow`**: The action is auto-approved without prompting.

> **Note**: Precedence Rule**: Conflicting rules are strictly evaluated in priority order: **Deny > Ask > Allow**. For example, if you configure `command(*)` in your `ask` list and `command(git)` in your `allow` list, the `ask` rule takes precedence and prompts before every command.

## Supported actions & matching rules

Fine-grained permissions follow a standard schema pattern:

```
action(target)
```

The supported actions, target format specifications, and matching algorithms are:

| Action | Target Format | Matching Behavior | Default Fallback |
| :-- | :-- | :-- | :-- |
| **`read_file`** | `read_file(/path)`, `read_file(dir)`, or `read_file(*)` | Matches absolute paths or paths relative to workspace roots. Grants recursive read access to all contained files/folders. `read_file(*)` matches all files on the system. | **Ask** (Auto-allowed in workspace) |
| **`write_file`** | `write_file(/path)` or `write_file(*)` | Same as `read_file`. Implicitly grants `read_file` for the exact same target path. | **Ask** (Auto-allowed in workspace) |
| **`read_url`** | `read_url(domain)` or `read_url(*)` | Matches hostnames and subdomains (e.g., `google.com` covers `mail.google.com`). Ignores URL path segments. `read_url(*)` matches any domain. | **Ask** |
| **`execute_url`** | `execute_url(domain)` or `execute_url(*)` | Actuating on web elements (clicking, typing) or driving interactive browser workflows on a domain. | **Ask** |
| **`command`** | `command(prefix)`, `command(regex)`, or `command(*)` | Matches commands by exact word/token prefix. Each whitespace-separated token is evaluated as an anchored regular expression (`^(?:pattern)$`).  
  
For example, `command(npm run (build|lint|test))` matches `npm run build` and `npm run test`. | **Ask** |
| **`unsandboxed`** | `unsandboxed(prefix)` or `unsandboxed(*)` | Matches commands by exact word/token prefix. Commands matching this grant will be executed outside of container isolation (only applicable when terminal sandboxing is enabled). | **Ask** |
| **`mcp`** | `mcp(server/tool)` or `mcp(*)` | Matches exact MCP tools or all tools on a specified server (applies to local `mcp` servers and remote connections). `mcp(*)` matches any tool. | **Ask** |

### Global wildcard syntax

Across all supported action types, passing the global wildcard `*` (such as `read_file(*)`, `command(*)`, `mcp(*)`) matches all targets within that entire action namespace.

### Implicit permission rules

*   **Write implies Read**: Allowing `write_file` on a path automatically grants `read_file` on that path.
*   **Deny Read implies Deny Write**: Denying `read_file` on a path immediately blocks `write_file` on that path.

### Cross-platform path normalization

Antigravity ensures your permission rules work flawlessly whether you are developing on macOS, Linux, or Windows. On macOS and Linux, paths use standard forward slashes (`/`). On Windows, Antigravity automatically normalizes paths prior to rule evaluation by stripping drive letters (e.g., `C:`) and converting all backslashes (`\`) to forward slashes (`/`).

* * *

## Default system behaviors & guardrails

When an action is not explicitly listed in your `allow`, `deny`, or `ask` lists, the system falls back to secure system defaults:

1.  **Workspaces are Auto-Allowed**: In standard operation, reading and writing files inside your active project directory is automatically allowed.
2.  **Web Browsing Defaults to Ask**: Actions for `read_url` and `execute_url` default to **Ask**. Before the agent navigates to or actuates on any web page, it will pause and prompt for your approval unless an allow rule is configured.
3.  **Unconfigured Actions Default to Ask**: All other unconfigured actions (`command`, `mcp`, `execute_url`, non-workspace files) default to **Ask**.

* * *

## Interactive permission prompts

When the agent encounters an operation requiring approval (**Ask** mode), an interactive prompt card appears in your TUI.

Before confirming **Allow** for file, URL, or MCP permissions, you can directly edit the target string in the prompt card to expand the granted scope (e.g., broadening a single file request like `/project/file.txt` to the parent directory `/project`). The CLI validates that your edited target safely covers the operation and applies the expanded grant for the remainder of the turn, preventing repeated prompts for related operations. _(Note: Scope editing is not supported for terminal commands)._

* * *

## Configuration examples

Add these rules to your `~/.gemini/antigravity-cli/settings.json` file:

```
{
    "permissions": {
        "allow": [
            "command(git)",
            "command(npm run (build|lint|test))",
            "unsandboxed(git push)",
            "read_file(/var/log/app)",
            "write_file(src/)",
            "read_url(google.com)",
            "mcp(linter/*)"
        ],
        "deny": [
            "command(rm -rf)",
            "command(curl .*)",
            "command(sudo)",
            "write_file(.git/)",
            "write_file(/home/user/.ssh)"
        ],
        "ask": ["command(*)", "execute_url(aws.amazon.com)", "mcp(sql/execute_mutation)"]
    }
}
```

## See also

*   **[Permissions Command](/docs/cli/commands/permissions)**: Manage rules interactively in the TUI.
*   **[Sandbox Customization](/docs/cli/sandbox)**: Enforce OS-level container isolation boundaries.
*   **[Plugins & Skills](/docs/cli/plugins)**: Create your own custom skills slash commands.
*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Customize keyboard hotkeys and buffers.

# Projects

Manage projects and organize conversation sessions in the Antigravity CLI.

## Launching sessions with projects

### 1\. Default project execution

When starting the CLI without any project flags, all conversations in the session will be in the `default-cli-project`:

```
agy
```

### 2\. Opening a session in a specific project

If you want to open a session attached to a specific existing project, pass the `--project` flag with the target project ID:

```
agy --project=<project_id>
```

### 3\. Creating a new project on startup

If you want to create a brand new project and initialize your CLI session inside it, pass the `--new-project` flag:

```
agy --new-project
```

### 4\. Resuming an existing conversation

If you resume a conversation (whether on startup via `--conversation=<conv_id>` or during a session using `/resume`), the conversation’s associated project will automatically be used.

## Moving conversations between projects (`/fork`)

While interacting in an active session, you can copy and continue your current conversation to a different project using the `/fork` slash command:

```
/fork <project_id>
```

When executed, the CLI forks your current conversation and associates the newly created conversation with `<project_id>`.

# Settings, rendering & keybindings

Configure persistent preferences, customize keyboard shortcuts, toggle terminal display buffers, and manage runtime CLI parameter overrides.

## Setting up preferences

Antigravity CLI stores user preferences in a minimal, forward-compatible JSON configuration profile.

### Configuration file location

The persistent settings are saved in a plain JSON format:

```
~/.gemini/antigravity-cli/settings.json
```

The CLI leverages **sparse persistence** by writing only values to disk that differ from their system defaults. This keeps your configuration file clean, minimal, and fully forward-compatible with future updates.

### The interactive settings panel

To edit settings directly inside your active terminal session without opening raw JSON files:

1.  Type `/config` (or its alias `/settings`) inside the prompt panel and press `Enter`.
2.  The full-screen **Settings Editor Overlay** opens.
3.  Navigate between available options using `↑`/`↓`.
4.  Press `Enter` on a highlighted parameter to toggle its state or open a text insertion field.
5.  Press `Esc` to save your modifications and close the editor.

![The interactive settings panel](/assets/image/docs/cli/settings-interactive-panel.png)

## Command-line overrides

You can temporarily override persistent preferences for individual terminal sessions using CLI command flags:

```
agy --sandbox --model="Gemini 3.5 Flash"
```

When an override flag is active, the interactive `/config` menu displays a warning indicator alongside the modified setting:

```
! Tool Permission: strict (overridden by command flag)
```

You can still edit the persistent value on disk during these sessions, but the CLI enforces the active runtime flag override until you close the session.

## Visual rendering modes

The TUI operates in one of two visual rendering modes depending on your terminal capability and connection latency.

### Alt-screen mode (`always`)

This mode opens a dedicated display screen using the terminal’s alternate buffer, creating an immersive, standalone app interface.

*   **Key features**: Integrated scrollback, mouse-wheel scrolling support, custom rendered scrollbar, and clean terminal state restoration on exit.
*   **Best used for**: Standard local development sessions in advanced terminal emulators (such as iTerm2, Ghostty, or WezTerm).

### Inline mode (`never`)

This mode renders output sequentially directly within your terminal’s standard stdout pipeline.

*   **Key features**: Preserves entire session history inside your emulator’s native scrollback buffer, does not capture mouse inputs, and works seamlessly alongside standard command outputs.
*   **Best used for**: Remote SSH terminals, terminal multiplexers like `tmux` or `screen`, and low-bandwidth remote sessions.

> **Note**: Adaptive Rendering**: Setting Alt-Screen mode to `default` allows the TUI to automatically detect your environment. It defaults to Alt-Screen on advanced local shells and degrades to Inline mode when running over SSH or in non-interactive sessions.

## Configuration options reference

The interactive settings panel (`/config`) and `settings.json` allow you to customize the CLI’s behavior across several categories.

### Safety & permissions

Manage how the agent interacts with your system and codebase:

*   **Tool Permission (`toolPermission`)**: Controls the authorization flow for tools (such as running terminal commands).
    *   `request-review` (Default): Prompts for your approval before running write, bash, or web tools.
    *   `proceed-in-sandbox`: Automatically runs terminal commands if they are sandboxed; otherwise prompts for review.
    *   `strict`: Prompts for all non-read tools, ensuring maximum control.
    *   `always-proceed`: Runs all tools without prompting (highest risk, use with caution).
*   **Artifact Review (`artifactReviewPolicy`)**: Controls when the agent prompts you to review generated artifacts (like code files) before writing them to disk.
    *   `asks-for-review` (Default): Always prompts you to review changes.
    *   `agent-decides`: The agent decides whether to prompt based on the complexity of the change.
    *   `always-proceed`: The agent writes changes directly without prompting (maximizes autonomy, but increases risk of overwriting code without review).
*   **Sandbox Mode (`enableTerminalSandbox`)**: When enabled (`on`), restricts all agent-initiated terminal commands to a secure OS container.
*   **Non-Workspace Access (`allowNonWorkspaceAccess`)**: Controls whether the agent can read or write files outside your active project directories. Set to `off` by default for safety.

### Display & rendering

Customize the visual experience of the TUI:

*   **Rendering Mode (`altScreenMode`)**: Controls how the TUI utilizes your terminal buffer.
    *   `default`: Adaptive mode. Uses Alt-screen on advanced local terminals and degrades to inline mode over SSH.
    *   `always`: Forces Alt-screen mode, providing an immersive, page-based interface with mouse support and scrollbars.
    *   `never` (configurable via `settings.json`): Forces inline mode, rendering output sequentially and preserving history in your emulator’s scrollback.
*   **Color Scheme (`colorScheme`)**: Selects the visual theme. Options include `terminal` (inherits shell colors), `dark`, `light`, `solarized dark/light`, `tokyo night`, and colorblind-friendly variants.
*   **Animation Speed (`runningLightSpeed`)**: Adjusts the speed of the progress indicator animation (`fast`, `medium`, `slow`, or `off`).
*   **Verbosity (`verbosity`)**: Controls detail level. `high` shows full agent thoughts and tool steps; `low` shows only minimal progress indicators.

### Editor & notifications

Configure integrations with your host environment:

*   **Editor (`editor`)**: The text editor used to view artifacts or compose prompts (via `Ctrl+G`). Defaults to `auto` (respects `$EDITOR`), but can be set to `vim`, `emacs`, or others.
*   **Editor Mode (`editorMode`)**: The editing model used inside the CLI prompt itself. Defaults to `default` (flat text editing); set it to `vim` for modal editing. See [Vim Editor Mode](/docs/cli/vim-editor-mode). This is independent of the `editor` setting above, which only selects an external program.
*   **Notifications (`notifications`)**: When enabled (`on`), triggers a system desktop notification and a terminal bell chime when a long-running task completes or requires your attention.

### AI Credits & Feedback

Manage usage, tips, and telemetry:

*   **Use AI Credits (`useG1Credits`)**: _External builds only._ When enabled (`on`), allows the CLI to use your personal AI credits for model calls if your plan’s standard quota is exhausted.
*   **Enable Telemetry (`enableTelemetry`)**: Helps Google improve the tool by sending anonymous usage statistics and crash reports.
*   **Show Tips (`showTips`)**: Toggles the display of helpful usage tips while the agent is generating responses.
*   **Show Feedback Survey (`showFeedbackSurvey`)**: Enables periodic brief surveys after task completions to help improve the experience.

## Custom status lines & terminal titles

For advanced TUI environment integrations, you can toggle active metrics or deploy custom scripts to generate dynamic status bars and modify your terminal window titles:

*   **[Status Line Customization](/docs/cli/commands/statusline)**: Learn how to manage the status indicator panel and construct custom formatted status line shell scripts.
*   **[Terminal Title Customization](/docs/cli/commands/title)**: Learn how to toggle window title outputs and pipe live agent states into your window headers.

## Keybindings configuration

You can customize almost all keyboard shortcuts in the TUI by mapping keys to specific workspace commands.

### Keybindings file location

Custom maps are stored alongside your primary settings profile:

```
~/.gemini/antigravity-cli/keybindings.json
```

### Format and customization

The JSON structure maps a single TUI command action to an array of hotkey sequences:

```
{
    "cli.clear_screen": ["ctrl+l"],
    "prompt.insert_newline": ["shift+enter", "ctrl+j"],
    "edit.open_editor": ["ctrl+g"]
}
```

To completely disable a default hotkey, map its action to an empty array `[]`. If your JSON schema is malformed or invalid, the CLI falls back to system defaults for those specific actions and loads the remaining valid mappings.

> **Note**: Protected Keys**: Crucial navigation shortcuts like `cli.exit` (`Ctrl+D` / `Ctrl+C`) and `cli.enter` (`Enter`) are protected by the system and cannot be disabled.

### Restoring defaults

To revert all keys back to system defaults, delete the keybindings profile:

```
rm ~/.gemini/antigravity-cli/keybindings.json
```

## Next steps

Now that you have configured your environment, review security controls and extensibility options:

*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Manage secure execution containment boundaries.
*   **[Plugins & Skills](/docs/cli/plugins)**: Create your own custom skills and import legacy plugins.
*   **[CLI Reference](/docs/cli/reference)**: Access quick reference sheets listing all configuration options, commands, and default key maps.

# Vim editor mode

Edit prompts with modal Vim keybindings instead of the default flat text editor.

Vim editor mode replaces the editing model in every multi-line input surface of the CLI:

| Surface | What you edit there |
| :-- | :-- |
| The prompt box | Your message to the agent, including multi-line prompts and slash commands. |
| The comment editor in [`/diff`](/docs/cli/commands/diff) | Review comments you leave on a changed file. |
| The comment editor in the artifact review panel | Feedback on a generated [artifact](/docs/cli/artifacts) before you accept it. |

It also adds a `vim` tab to the help overlay and a mode badge to the [status line](/docs/cli/statusline).

## Enable Vim editor mode

Vim editor mode is off by default. Turn it on from the interactive settings panel or directly in `settings.json`.

### Using the settings panel

1.  Type `/settings` inside the prompt panel and press `Enter`.
    
2.  Navigate to **Editor Mode** using `↑`/`↓`.
    
3.  Press `Enter` to select `vim`.
    
4.  Set **Editor Mode › Insert First** to choose which mode each prompt starts in. Leave it `off` to start in Normal mode, or set it `on` to start in Insert mode with a bare `Enter` that submits. See [Start in Insert mode](#start-in-insert-mode).
    
5.  Press `Esc` to save and close the editor.
    

### Using `settings.json`

Set `editorMode` in your configuration profile:

```
{
    "editorMode": "vim",
    "vimInsertFirst": false
}
```

The CLI loads this file from `~/.gemini/antigravity-cli/settings.json` at startup. `editorMode` accepts `"default"` and `"vim"`. `vimInsertFirst` controls which mode each new prompt starts in and applies only when `editorMode` is `"vim"`; see [Start in Insert mode](#start-in-insert-mode).

> **Note:** `editorMode` is unrelated to the [`editor` setting](/docs/cli/settings). `editor` picks the external program that `Ctrl+G` launches, so setting `editor` to `"vim"` opens Vim in a separate window and does nothing to the prompt. `editorMode` is the one that controls modal editing inside the CLI prompt itself.

## Switch between modes

Vim editor mode starts in NORMAL. Press `i` to type, and `Esc` to return to NORMAL.

| Command | Action | From mode |
| :-- | :-- | :-- |
| `Esc`, `Ctrl+C` | Enter NORMAL mode | INSERT, VISUAL |
| `i` | Insert before the cursor | NORMAL |
| `I` | Insert at the first non-blank character | NORMAL |
| `a` | Insert after the cursor | NORMAL |
| `A` | Insert at the end of the line | NORMAL |
| `o` | Open a line below and insert | NORMAL |
| `O` | Open a line above and insert | NORMAL |
| `v` | Start a character-wise selection | NORMAL |
| `V` | Start a line-wise selection | NORMAL |

The status line reports the current mode:

| Mode | Badge |
| :-- | :-- |
| NORMAL | none |
| INSERT | `-- INSERT --` |
| VISUAL | `-- VISUAL --` |
| VISUAL LINE | `-- V-LINE --` |

An empty badge area means you are in NORMAL mode. If you run a [custom status line](#show-the-mode-in-a-custom-status-line), it replaces this badge unless you stack it with the default.

> **Tip:** Press `?` in NORMAL mode to open the shortcuts overlay, or run `/help` and select the `vim` tab for a full cheat sheet.

## Submit your prompt

Enter behaves differently in each mode, so you can compose multi-line prompts without accidental submits.

| Context | `Enter` | `Ctrl+S` / `Ctrl+Enter` | `ZZ` |
| :-- | :-- | :-- | :-- |
| NORMAL mode | Submit | Submit | Submit |
| INSERT mode | Insert a newline | Submit | — |
| INSERT mode, insert-first on | Submit | Submit | — |

`ZZ` submits from NORMAL and VISUAL mode, matching the muscle memory of writing and quitting a buffer.

### Start in Insert mode

Set `vimInsertFirst` when you want each new prompt to begin in INSERT mode with a bare `Enter` that submits. This keeps the default typing experience while leaving NORMAL mode one `Esc` away.

```
{
    "editorMode": "vim",
    "vimInsertFirst": true
}
```

The **Editor Mode › Insert First** option appears in `/settings` only when Editor Mode is set to `vim`. It has no effect in default mode.

## Move the cursor

All motions work on their own in NORMAL and VISUAL mode, and as targets for an operator.

| Key | Motion |
| :-- | :-- |
| `h` `l` | Left, right |
| `j` `k` | Down, up |
| `0` `$` | Start of line, end of line |
| `^` | First non-blank character on the line |
| `w` `b` `e` | Next word, previous word, end of word |
| `W` `B` `E` | Same, treating whitespace-delimited chunks as words |
| `gg` `G` | Start of input, end of input |
| `f{char}` `F{char}` | Jump onto the next or previous `{char}` |
| `t{char}` `T{char}` | Stop one character short of the next or previous `{char}` |
| `;` `,` | Repeat the last `f`/`F`/`t`/`T` forward, backward |

## Edit text

Editing commands fall into three groups: single keys that act immediately, operators that wait for a motion, and text objects that select a delimited region.

### Single-key commands

| Key | Action |
| :-- | :-- |
| `x` | Delete the character under the cursor |
| `r{char}` | Replace the character under the cursor with `{char}` |
| `D` `C` | Delete or change from the cursor to the end of the line |
| `o` `O` | Open a new line below or above and enter INSERT mode |
| `p` `P` | Paste after or before the cursor |
| `u` `U` | Undo, redo. `Ctrl+R` does not redo; it opens artifact review |

Commands take no count prefix, so `3dd` deletes one line. To act on several lines at once, select them with `V` and press the operator. There is also no `.` to repeat the last change.

There is one unnamed register rather than the usual `"a`–`"z` set. Deletes fill it, so `x`, `D`, `C`, `d`, and `c` all leave text you can paste back with `p`.

Paste is linewise-aware. Text yanked with `dd` or `yy` pastes onto a new line below (`p`) or above (`P`). Anything else pastes inline.

### Operators and motions

Combine an operator with any motion to act on the span it covers.

| Operator | Action | Word forms | Whole line |
| :-- | :-- | :-- | :-- |
| `d` | Delete | `dw` `de` `db` | `dd` |
| `c` | Change (delete, then enter INSERT mode) | `cw` `ce` `cb` | `cc` |
| `y` | Yank | `yw` `ye` `yb` | `yy` |

```
dw     Delete to the start of the next word
d$     Delete to the end of the line
c^     Change back to the first non-blank character
yG     Yank to the end of the input
dfx    Delete forward through the next "x"
```

`cw` changes to the end of the current word, matching real Vim.

### Text objects

Pair an operator with `i` (inside) or `a` (around) and a delimiter.

| Object | Selects |
| :-- | :-- |
| `iw` `aw` | A word, with or without surrounding whitespace |
| `iW` `aW` | A whitespace-delimited chunk |
| `i"` `a"` `i'` `a'` | Text in single or double quotes |
| `i(` `a(` `i)` `a)` | Text in parentheses |
| `i[` `a[` `i]` `a]` | Text in square brackets |
| `i{` `a{` `i}` `a}` | Text in braces |

Backticks work the same way: pair `i` or `a` with a backtick to select inline code.

```
ci"    Change the text inside the nearest quotes
da(    Delete a parenthesized group, parentheses included
yiw    Yank the word under the cursor
```

## Work with selections

Press `v` or `V` to select, move with any motion, then apply a command. Press `v` or `V` again, or `Esc`, to leave.

| Key | Action on the selection |
| :-- | :-- |
| `d` `x` | Delete |
| `c` | Change |
| `y` | Yank |
| `r{char}` | Replace every selected character with `{char}` |
| `~` | Toggle case |
| `u` `U` | Lowercase, uppercase |

> **Note:** `~`, `u`, and `U` change case in VISUAL mode only. In NORMAL mode, `u` and `U` are undo and redo.

## Run slash and shell commands

Press `/` or `!` in NORMAL mode. The CLI inserts the character and switches to INSERT mode, so slash commands and shell commands work without pressing `i` first.

```
/settings     Open the settings panel from NORMAL mode
!ls -la       Run a shell command from NORMAL mode
```

## Customize the submit and newline keys

Three Vim actions are remappable in `~/.gemini/antigravity-cli/keybindings.json`. These are the defaults:

```
{
    "vim.insert.insert_newline": ["alt+enter", "ctrl+j", "enter", "shift+enter"],
    "vim.insert.submit": ["ctrl+enter", "ctrl+s"],
    "vim.normal.submit": ["ctrl+enter", "ctrl+s"]
}
```

Motions, operators, and text objects are fixed and cannot be remapped.

### Submit with Enter in NORMAL mode only

This is the default. `Enter` submits from NORMAL mode and inserts a newline in INSERT mode, so you can type freely and submit with a single `Esc` `Enter`. No configuration is needed. Leave `vimInsertFirst` off:

```
{
    "editorMode": "vim",
    "vimInsertFirst": false
}
```

### Submit with Enter in INSERT mode too

Move `enter` out of `vim.insert.insert_newline` and into `vim.insert.submit`. `Shift+Enter`, `Alt+Enter`, and `Ctrl+J` still insert newlines:

```
{
    "vim.insert.insert_newline": ["alt+enter", "ctrl+j", "shift+enter"],
    "vim.insert.submit": ["ctrl+enter", "ctrl+s", "enter"]
}
```

Setting `vimInsertFirst` to `true` achieves the same submit behavior without editing keybindings, but it also changes which mode each new prompt starts in.

> **Warning:** `Enter` always submits in NORMAL mode. Remapping `vim.normal.submit` adds keys; it never removes `Enter`.

## Show the mode in a custom status line

A [custom status line](/docs/cli/statusline) replaces the built-in one, and the mode badge goes with it. You have two ways to get the mode back.

Keep the built-in line and stack your script underneath it:

```
{
    "statusLine": {
        "type": "command",
        "command": "~/.gemini/antigravity-cli/statusline.sh",
        "stack_with_default": true
    }
}
```

Or render the mode yourself. When `editorMode` is `"vim"`, the JSON payload piped to your script carries a `vim` object:

```
{
    "vim": {
        "mode": "INSERT"
    }
}
```

`mode` is `NORMAL`, `INSERT`, `VISUAL`, or `VISUAL LINE`. The field is absent entirely when Vim editor mode is off, so a script can use its presence as the enablement check:

```
#!/bin/bash
input=$(cat)
mode=$(echo "$input" | jq -r '.vim.mode // empty')
[ -n "$mode" ] && printf -- '-- %s -- ' "$mode"
echo "$input" | jq -r '.model.display_name'
```

> **Note:** `vim.mode` reports `NORMAL`, unlike the built-in badge, which renders nothing in that mode. A script that prints every mode shows a `-- NORMAL --` badge the built-in line never displays.

## Next steps

*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Configure the rest of your preferences and remap keys.
*   **[Status Line Customization](/docs/cli/statusline)**: Control what the status line reports alongside the Vim mode badge.
*   **[CLI Reference](/docs/cli/reference)**: Look up every configuration key and default keybinding.

# Managing AI Credits & Quotas

The Antigravity CLI integrates with your subscription to monitor and manage your AI Premium credits and usage quotas.

For a detailed explanation of baseline quotas, how credits are consumed, and plan eligibility, please refer to the main **[Plans](/docs/plans)** page.

## Quota Tracking

You can monitor your active quota and credit consumption directly inside the CLI:

*   **Statusline Indicator**: The right side of the CLI statusline displays your remaining credit count (e.g., `AI Credits: 42`).
*   **Low Quota Alert**: When your remaining AI credits drop below the warning threshold, the statusline indicator highlights to warn you that your limits are near.

## Slash Commands & Managing Balance

You can query your credits or buy additional quota directly from the CLI:

*   **Query Balance**: Run the **[AI Credits Command](/docs/cli/commands/credits)** to open the dedicated credits panel. This panel displays your detailed credit usage statistics.
*   **Managing Credits**: You can easily purchase AI credits or upgrade your subscription, which opens a panel containing direct pricing and subscription portal links.

## Settings Configuration

To control when and how your AI credits are used, you can toggle credit settings in your `settings.json` file:

```
{
    "useG1Credits": true
}
```

*   **Use AI Credits Option**: Run `/config` or `/settings` to open the CLI settings panel. Set the **Use G1 Credits** field to **on** to allow the CLI to use your personal credits when plan quotas are exhausted, or set it to **off** to restrict fallback billing. (To learn more, see the **[Plans](/docs/plans#overages)** overages section).

## See also

*   **[AI Credits Command](/docs/cli/commands/credits)**: View and manage your credits interactively in the TUI.
*   **[Model Quotas Command](/docs/cli/commands/usage)**: Monitor your model-specific API quotas.

# Model Context Protocol (MCP)

Antigravity supports the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), an open standard that lets AI agents and editors securely connect to local developer tools, databases, file parsers, and external remote APIs. This integration provides the AI model with real-time context and execution capabilities beyond your immediate workspace.

In this guide, you’ll learn how to connect and configure MCP servers across Antigravity products. You can also skip to information for MCP servers in [Antigravity 2.0](/docs/mcp#antigravity-20), [Antigravity IDE](/docs/mcp#antigravity-ide), [Antigravity CLI](/docs/mcp#antigravity-cli), or [Antigravity SDK](/docs/mcp#antigravity-sdk).

## What is MCP?

MCP acts as a universal bridge between Antigravity and your broader development environment. Instead of manually copying and pasting database schemas, logs, or API specifications into prompts or chat panels, MCP lets Antigravity fetch structured context directly or execute safe actions on your behalf when needed.

### Add Context

With MCP, Antigravity can use live data from connected MCP servers to inform its reasoning and suggestions:

*   When writing a SQL query, Antigravity can inspect your live Neon, Supabase, or AlloyDB schema to suggest correct table and column names.
*   When debugging deployment failures, Antigravity can pull recent build logs directly from Netlify or Heroku.

### Add Custom Tools

With MCP, Antigravity can execute specific, safe actions defined by your connected servers:

*   Create a Linear issue for this TODO.
*   Search Notion or GitHub for authentication patterns.

## Antigravity 2.0

In Antigravity 2.0, you can manage your MCP servers through the **Installed MCP Servers** section of your **Settings**.

To view and update your MCP servers:

1.  Click the **Settings** button found on the bottom left of your screen.
2.  Select **Customizations** and review the **Installed MCP Servers** section.

To install an MCP server from the **Installed MCP Servers** section:

1.  Click **Add MCP**. This will connect you to the MCP Store, a searchable list of available MCP servers.
2.  Search or scroll down to an MCP server you’d like to install.
3.  Click **Add**.

To manage your MCP servers from this screen:

*   **Uninstall**: Click the trash can icon next to the MCP server in the list.
*   **Disable/enable**: Click the toggle switch next to the MCP server in the list.
*   **Refresh**: Click the refresh button.

## Antigravity IDE

In Antigravity IDE, the easiest way to manage MCP servers is through the built-in MCP Store. In the MCP Store, you can browse, discover, and install supported MCP servers. You can also install custom servers by updating your `mcp_config.json`.

To use the MCP Store:

1.  Click **…** at the top of the editor’s agent side panel and select **MCP Servers**.
2.  Hover over any supported server and click **Install**. (Or, click a server to view details and then click **Install**.)
3.  Follow any on-screen prompts.

Once installed, resources and tools from the server are automatically available to the editor.

To connect to a custom MCP server not listed in the store:

1.  Click **…** at the top of the editor’s agent side panel and select **MCP Servers**.
2.  Click **Manage MCP Servers**.
3.  Click **View raw config**.
4.  Modify the `mcp_config.json` file with your custom [MCP server configuration](/docs/mcp#mcp-configuration-structure).

The configuration file is located globally at `~/.gemini/config/mcp_config.json` (or locally in your workspace under `.agents/mcp_config.json`).

## Antigravity CLI

Antigravity CLI supports both local `stdio` processes and remote host MCP server configurations. The simplest path to installing an MCP server on Antigravity CLI is by using the **Interactive MCP Manager**. You can also manually edit your global server setup or workspace-level `mcp_config.json`.

### Interactive MCP Manager

Type `/mcp` inside the prompt panel and press `Enter` to open the interactive **MCP Manager Overlay**. This panel lets you:

*   View live status rings for active, disconnected, or loading servers.
*   Manually reload server configurations or inspect real-time connection logs.

### Global and Workspace Server Configs

Unlike legacy setups, Antigravity CLI separates MCP definitions into dedicated, sparse configurations:

*   **Global server setups:** Configured in `~/.gemini/config/mcp_config.json`.
*   **Workspace local setups:** Configured in your active project under `.agents/mcp_config.json`.

You can modify these files directly with your custom [MCP server configuration](/docs/mcp#mcp-configuration-structure).

> **Note**: Remote Connection Schema**: When declaring remote SSE, Streamable HTTP, or websocket-based MCP connections, you must define the `serverUrl` field. Legacy fields like `url` or `httpUrl` are not supported.

## Antigravity SDK

In Python applications built using the [Antigravity SDK](/docs/sdk/overview), MCP servers (`stdio`, `SSE`, or `HTTP`) can be connected programmatically under a unified execution pipeline alongside built-in tools and custom Python functions.

The SDK automatically discovers servers configured in your workspace’s `.agents/mcp_config.json` file. You can also instantiate agents with local configurations directly:

```
import asyncio
from google.antigravity import Agent, LocalAgentConfig
```

## MCP Configuration Structure

Whether configuring custom servers for Antigravity 2.0, Antigravity IDE, or Antigravity CLI, the configuration file follows a standardized format. The file contains a single `mcpServers` object where you define each server you want to connect to:

```
{
  "mcpServers": {
    "sqlite-explorer": {
      "command": "node",
      "args": ["/usr/local/bin/sqlite-mcp-server.js"],
      "env": {
        "SQLITE_DB_PATH": "/var/data/app.db"
      }
    },
    "my-remote-server": {
      "serverUrl": "https://api.example.com/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

### MCP Configuration Properties

Each server entry under `mcpServers` supports the following properties:

**Transport (one required):**

*   **`command`** (string): Path to the executable for `stdio` transport.
*   **`serverUrl`** (string): URL for remote `Streamable HTTP` or `SSE` servers.

**Optional:**

*   **`args`** (string\[\]): Command-line arguments for `stdio` transport.
*   **`env`** (object): Environment variables for the `stdio` server process.
*   **`cwd`** (string): Working directory for `stdio` servers.
*   **`headers`** (object): Custom HTTP headers for remote servers.
*   **`authProviderType`** (string): Authentication provider. Supports `"google_credentials"` for Google Application Default Credentials (ADC).
*   **`oauth`** (object): OAuth client credentials (`clientId`, `clientSecret`).
*   **`disabled`** (boolean): Temporarily disable a server without removing its configuration.
*   **`disabledTools`** (string\[\]): Tool names to withhold from the model.

## MCP Authentication

Connected MCP servers can securely authenticate against external services using built-in Google credentials, automatic OAuth flows, or custom HTTP headers.

### Google Credentials

Set `authProviderType` to `"google_credentials"` to use Google Application Default Credentials (ADC).

```
{
  "mcpServers": {
    "my-gcp-service": {
      "serverUrl": "https://example.googleapis.com/mcp/",
      "authProviderType": "google_credentials"
    }
  }
}
```

This requires Application Default Credentials to be configured locally. To set them up, run:

```
gcloud auth application-default login
```

If you previously logged in, ensure your quota project is set by running:

```
gcloud auth application-default set-quota-project {QUOTA_PROJECT}
```

### OAuth

Antigravity can automatically handle OAuth for servers that support dynamic client registration (DCR). For these servers, no additional configuration is needed:

```
{
  "mcpServers": {
    "oauth-server": {
      "serverUrl": "https://api.example.com/mcp/"
    }
  }
}
```

If the server does not support dynamic client registration, you can provide your client credentials manually:

```
{
  "mcpServers": {
    "oauth-server": {
      "serverUrl": "https://api.example.com/mcp/",
      "oauth": {
        "clientId": "your-client-id",
        "clientSecret": "your-client-secret"
      }
    }
  }
}
```

If you provided client credentials manually, ensure the following is registered as a redirect URI in your OAuth provider:

```
https://antigravity.google/oauth-callback
```

When connecting to an OAuth-enabled server:

1.  Open [**Agent Settings**](/docs/settings) with `Cmd+,` (Mac) or `Ctrl+,` (Windows/Linux).
    
2.  Navigate to the **Customizations** tab and click the **Authenticate** button next to the server.
    
    ![Click Authenticate](/assets/image/docs/tools/mcp-oauth-authenticate.png)
    
3.  Complete authentication in your browser and copy the authorization code.
    
    ![Copy authorization code](/assets/image/docs/tools/mcp-oauth-copy-code.png)
    
4.  Paste the code back into the settings panel and click **Submit**.
    
    ![Paste auth code](/assets/image/docs/tools/mcp-oauth-paste-code.png)
    

Once authenticated, the server will reconnect automatically.

![Authenticated server](/assets/image/docs/tools/mcp-oauth-authenticated.png)

Access tokens are stored in `~/.gemini/antigravity/mcp_oauth_tokens.json`. Expired tokens are refreshed automatically, and invalid tokens are removed.

### Custom Headers

For remote servers that require custom HTTP headers (e.g. API keys or bearer tokens), add them to the `headers` object. For example:

```
{
  "mcpServers": {
    "my-remote-server": {
      "serverUrl": "https://api.example.com/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_TOKEN"
      }
    }
  }
}
```

## MCP Permissions and Access Control

Access to Model Context Protocol tools and resources is governed by Antigravity’s [permissions system](/docs/permissions). By default, unconfigured MCP tools run in **Ask** mode, requiring your approval before execution. You can allow specific tools or entire servers in your policy configuration:

*   `mcp(server/tool)`: Matches a specific tool on a specific server.
*   `mcp(server/*)`: Matches all tools on a specified server.
*   `mcp(*)`: Global wildcard matching any MCP tool across all connected servers.

## Supported MCP Servers

The MCP Store features direct integrations for a wide variety of developer platforms, databases, and productivity services:

Databases & Storage (14 servers)

*   AlloyDB for PostgreSQL
*   BigQuery
*   Bigtable Admin remote MCP
*   ClickHouse
*   Cloud SQL (MySQL, PostgreSQL, SQL Server, Managed)
*   Dataplex
*   MCP Toolbox for Databases
*   MongoDB
*   Neon
*   Pinecone
*   Prisma
*   Redis
*   Spanner
*   Supabase

Developer Tools & CI/CD (13 servers)

*   Apigee MCP
*   Atlassian
*   Cloud CLI Execution
*   GitHub
*   GitLab Orbit
*   GKE OneMCP
*   Harness
*   Heroku
*   Home Developer MCP
*   Linear
*   Netlify
*   Postman
*   SonarQube

Frontend & Design (6 servers)

*   Chrome DevTools
*   Dart
*   Figma Dev Mode MCP
*   Locofy
*   Lovable MCP
*   Mobbin MCP

Analytics, AI & Cloud (13 servers)

*   Airweave
*   Antimetal
*   Arize
*   Firebase
*   Google Cloud Quotas
*   Looker
*   Notion
*   PayPal
*   Perplexity Ask
*   PostHog
*   Sequential Thinking
*   Stripe
*   Windsor AI

# Plugins & skills

Extend agent capabilities, install third-party extension bundles, package custom workflow skills, and interface with Model Context Protocol (MCP) servers.

## The extensibility model

Antigravity CLI is designed for limitless customization. You can augment the shared agent harness by installing structured package modules called **Plugins** or creating localized markdown blueprints called **Skills**.

These customizations allow agents to access specialized proprietary commands, invoke domain-specific subagents, and consult customized style constraints.

## Antigravity plugins

Plugins are namespaced bundles that package custom skills, background subagents, linting rules, Model Context Protocol definitions, and event hooks into a single deployable asset.

### Plugin filesystem structure

When you install or import a plugin, the CLI stages the bundle files within your global configuration path:

```
~/.gemini/antigravity-cli/plugins/<plugin_name>/
```

A compliant plugin contains the following layout:

```
~/.gemini/antigravity-cli/plugins/<plugin_name>/
├── plugin.json                 # Required package marker file
├── mcp_config.json             # Optional Model Context Protocol servers
├── hooks.json                  # Optional pre/post tool event hooks
├── skills/                     # Optional specialized skills directory
├── agents/                     # Optional subagent definition templates
└── rules/                      # Optional custom codebase rules files
```

### The plugin manifest (plugin.json)

The `plugin.json` file is a mandatory manifest located at the root of your plugin directory. It defines the plugin’s identity and metadata.

**Manifest example**

```
{
    "$schema": "https://antigravity.google/schemas/v1/plugin.json",
    "name": "my-plugin",
    "description": "A brief description of what my plugin does."
}
```

**Field reference**

| Field | Type | Required | Description |
| :-- | :-- | :-- | :-- |
| `name` | String | **Yes** | The unique, machine-readable name of the plugin. It must contain only alphanumeric characters, hyphens, and underscores (matches `^[a-zA-Z0-9-_]+$`). This name is used to reference the plugin in CLI commands. |
| `description` | String | No | A brief human-readable description of the plugin’s purpose, displayed in plugin listings. |

**Automatic validation**

To enable automatic autocomplete and validation in editors like VS Code or WebStorm, include the `$schema` key pointing to the official schema URL:

```
"$schema": "https://antigravity.google/schemas/v1/plugin.json"
```

**Full JSON Schema**

```
{
    "$schema": "https://antigravity.google/schemas/v1/plugin.json",
    "title": "Antigravity Plugin Manifest",
    "description": "Schema for Antigravity CLI plugin manifest files (plugin.json)",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "The unique, machine-readable name of the plugin. Must contain only alphanumeric characters, hyphens, and underscores.",
            "pattern": "^[a-zA-Z0-9-_]+$"
        },
        "description": {
            "type": "string",
            "description": "A brief human-readable description of the plugin's purpose and capabilities."
        }
    },
    "required": ["name"],
    "additionalProperties": false
}
```

### Managing plugins via CLI subcommands

The CLI exposes a `plugin` (or plural `plugins`) subcommand pipeline to manage your extensions:

*   **List installed plugins**: Show active packages and their loaded components.
    
    ```
    agy plugin list
    ```
    
*   **Install a local or remote plugin**: Stage a package directory into your local profile.
    
    ```
    agy plugin install /path/to/local/plugin
    ```
    
*   **Disable/Enable a plugin**: Suspend a plugin’s tools without deleting its assets.
    
    ```
    agy plugin disable <plugin_name>
    agy plugin enable <plugin_name>
    ```
    
*   **Uninstall a plugin**: Purge the package directory and clean up registries.
    
    ```
    agy plugin uninstall <plugin_name>
    ```
    

## Agent skills

Skills are declarative, human-readable markdown files that outline explicit instruction protocols, scripts, and target resources for specialized engineering tasks.

Once registered, **Skills convert automatically into slash commands** inside the TUI, allowing you to invoke them manually (e.g., typing `/refactor-ui`).

### Creating local workspace skills

To deploy workspace-specific skills that stay with your git repository:

1.  Create a directory named `.agents/skills/` at your project root.
2.  Inside, draft a markdown file with a `.md` extension (such as `format-tests.md`).
3.  Define the skill’s Frontmatter metadata (see the example below).
4.  Below the metadata, write explicit instructions for the agent. When you run `agy` in this directory, the skill is compiled, and `/format-tests` becomes available in the prompt box.

**Frontmatter example:**

```
---
name: format-tests
description: Standardize and re-format Python unittest assertions
---
```

### Sharing global skills

To share skills across all workspaces on your workstation, place the target markdown files inside your global configuration path:

```
~/.gemini/antigravity-cli/skills/
```

Any markdown skill in this directory is automatically imported as a global slash command whenever you launch `agy` in any directory.

## Managing hooks

Hooks intercept agent actions right before or immediately after execution. They are useful for running automated pre-flight checks or post-generation formats (such as running `prettier` after writing files).

Hooks are defined inside a plugin’s `hooks.json` or configured inside your primary `settings.json` file. You can inspect all loaded and active hooks inside the TUI by typing:

```
/hooks
```

## Model Context Protocol (MCP)

Model Context Protocol is an open standard enabling foundation models to interface securely with local APIs, file parsers, and custom developer tools.

For comprehensive documentation on configuring local and remote MCP servers in Antigravity CLI, accessing the interactive `/mcp` manager overlay, and understanding server schemas and authentication, see the dedicated [MCP Documentation](/docs/mcp).

## Next steps

Learn how to migrate your existing configurations from Gemini CLI and troubleshoot connection anomalies:

*   **[Migration from Gemini CLI](/docs/cli/gcli-migration)**: Fast-track your legacy extensions and config conversions.
*   **[Troubleshooting](/docs/cli/troubleshooting)**: Resolve terminal hook errors, lockouts, or network failures.
*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Configure security containment rings around your custom plugins and MCP servers.

# Status line customization

Define custom scripting configurations and format dynamic JSON state payloads to customize your TUI status line.

Note

To toggle the status line on/off or configure it from the TUI, see the **[Status Line Command](/docs/cli/commands/statusline)**.

## Overview

The status line is positioned at the bottom of the TUI prompt panel. It provides at-a-glance context regarding active agent cycles, workspace environments, context token window usages, and background execution tasks.

## Custom status line scripting

For advanced terminal layouts or custom status bar displays, you can route active agent metadata into a custom script.

### Configuration

Add a `statusLine` configuration block to your `~/.gemini/antigravity-cli/settings.json` file:

```
{
    "statusLine": {
        "type": "command",
        "command": "~/.gemini/antigravity-cli/statusline.sh"
    }
}
```

Whenever the agent state changes, the TUI executes your command script, pipes a detailed state JSON payload directly to the script’s `stdin`, reads your formatted string from `stdout`, and renders the result in the prompt’s status line. Full ANSI color codes are supported.

The block accepts three more optional keys: `padding` adds blank lines above the status line, `enabled` set to `false` suspends the script while keeping the command on file, and `stack_with_default` set to `true` renders your script below the built-in line instead of replacing it.

### Available JSON fields

The JSON payload piped to your script contains the following top-level fields:

| Field | Type | Description |
| :-- | :-- | :-- |
| `cwd` | string | Current working directory when the CLI was launched. |
| `session_id` | string | Backward-compatibility alias for `conversation_id`. |
| `conversation_id` | string | Current unique conversation ID. |
| `transcript_path` | string | Absolute path to the active conversation transcript log file (optional). |
| `model` | object | Contains `id` and `display_name` of the active model. |
| `workspace` | object | Contains `current_dir` and `project_dir` paths. |
| `version` | string | CLI version string. |
| `context_window` | object | Contains token usage details: `total_input_tokens`, `total_output_tokens`, `context_window_size`, `used_percentage`, `remaining_percentage`, and `current_usage` sub-object. |
| `exceeds_200k_tokens` | bool | True if the conversation context has exceeded 200k tokens (null before first API call). |
| `product` | string | Application name (e.g., `antigravity`). |
| `quota` | object | Maps model/bucket IDs to their quota status, containing `remaining_fraction`, `reset_time`, and `reset_in_seconds` (optional). |
| `agent_state` | string | Current state: `idle`, `thinking`, `working`, `tool_use`, `initializing`. |
| `vcs` | object | Version control info: `type` (git/jj/hg), `branch`, `client`, `dirty` (optional). |
| `sandbox` | object | Sandbox configuration: `enabled`, `allow_network` (optional). |
| `artifact_count` | int | Number of artifacts produced in the conversation. |
| `plan_tier` | string | Subscription tier of the authenticated user (optional). |
| `email` | string | Email/LDAP of the authenticated user. |
| `pending_input_count` | int | Number of queued user messages. |
| `tool_confirmation_pending` | bool | True when a tool confirmation dialog is showing. |
| `task_count` | int | Number of running background tasks. |
| `terminal_width` | int | Live width of the interactive terminal. |
| `execution_mode` | string | Current active prompt execution mode (e.g., `planning`, `fast`). |
| `vim` | object | Vim editing state: `mode` is `NORMAL`, `INSERT`, `VISUAL`, or `VISUAL LINE`. Present only when [Vim editor mode](/docs/cli/vim-editor-mode) is enabled. |

### JSON payload example

Here is a fully sanitized, typical JSON payload piped to your status line script:

```
{
    "cwd": "/home/user/my-project",
    "session_id": "12345678-abcd-ef01-2345-6789abcdef01",
    "conversation_id": "12345678-abcd-ef01-2345-6789abcdef01",
    "transcript_path": "/home/user/.gemini/antigravity/brain/12345678-abcd-ef01-2345-6789abcdef01/.system_generated/logs/transcript.jsonl",
    "model": {
        "id": "Gemini 3.5 Flash (High)",
        "display_name": "Gemini 3.5 Flash (High)"
    },
    "workspace": {
        "current_dir": "/home/user/my-project",
        "project_dir": "/home/user/my-project"
    },
    "version": "1.0.13",
    "context_window": {
        "total_input_tokens": 88244,
        "total_output_tokens": 61074,
        "context_window_size": 1048576,
        "used_percentage": 14.24,
        "remaining_percentage": 85.76,
        "current_usage": {
            "input_tokens": 63382,
            "output_tokens": 346,
            "cache_creation_input_tokens": 0,
            "cache_read_input_tokens": 20857
        }
    },
    "exceeds_200k_tokens": false,
    "product": "antigravity",
    "quota": {
        "gemini-weekly": {
            "remaining_fraction": 0.9378,
            "reset_time": "2026-07-06T07:50:32Z",
            "reset_in_seconds": 560580
        }
    },
    "agent_state": "idle",
    "vcs": {
        "type": "git",
        "branch": "main",
        "dirty": false
    },
    "sandbox": {
        "enabled": false
    },
    "artifact_count": 2,
    "plan_tier": "Pro",
    "email": "developer@email.com",
    "task_count": 1,
    "terminal_width": 111,
    "execution_mode": "planning"
}
```

### Example script

You can download a complete, layout-adaptive script from the official [statusline.sh example on GitHub](https://github.com/google-antigravity/antigravity-cli/blob/main/examples/statusline/statusline.sh). This script renders state badges, handles active branches, and formats context window progress bars dynamically.

Save the script to `~/.gemini/antigravity-cli/statusline.sh` and make it executable:

```
chmod +x ~/.gemini/antigravity-cli/statusline.sh
```

## See also

*   **[Status Line Command](/docs/cli/commands/statusline)**: Toggle status line elements interactively.
*   **[Terminal Title Customization](/docs/cli/title)**: Configure dynamic window titles.
*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Customize keyboard hotkeys and buffers.
*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Manage secure directory permissions.

# Terminal title customization

Configure dynamic window titles, map custom scripting configurations, and format JSON state outputs to customize terminal headers.

Note

To toggle or set the terminal title interactively, see the **[Window Title Command](/docs/cli/commands/title)**.

## Overview

The terminal window title feature displays agent details, active workspace basenames, and active conversation parameters inside your terminal emulator’s title bar. This lets you monitor agent progress even when the terminal window is minimized or unfocused.

## Custom title scripting

For customized window title formatting, you can route active TUI state details into a custom shell script.

### Configuration

Add a `title` configuration block to your `~/.gemini/antigravity-cli/settings.json` file:

```
{
    "title": {
        "type": "command",
        "command": "~/.gemini/antigravity-cli/title.sh"
    }
}
```

Whenever the agent state changes, the TUI executes your command script, pipes a detailed state JSON payload directly to the script’s `stdin`, reads your formatted string from `stdout`, and updates your terminal window title. Non-printable characters and ANSI escape sequences are automatically stripped before rendering.

### JSON state payload schema

The JSON state payload is the same as the one sent to the custom status line script. It includes detailed properties representing `cwd`, `conversation_id`, `agent_state`, `vcs` details, and more. See the **[Status Line Schema](/docs/cli/statusline#available-json-fields)** for the complete property list.

### Example script

You can download a complete, layout-adaptive script from the official [title.sh example on GitHub](https://github.com/google-antigravity/antigravity-cli/blob/main/examples/title/title.sh). This script extracts the active workspace folder basename and renders a structured terminal title containing live agent states and conversation session prefixes.

Save the script to `~/.gemini/antigravity-cli/title.sh` and make it executable:

```
chmod +x ~/.gemini/antigravity-cli/title.sh
```

## See also

*   **[Window Title Command](/docs/cli/commands/title)**: Toggle or set the terminal title interactively.
*   **[Status Line Customization](/docs/cli/statusline)**: Customize dynamic TUI status bars.
*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Customize keyboard hotkeys and buffers.
*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Manage secure directory permissions.

# Agents Command (/agents)

Browse, select, and switch between custom agents, or monitor active and completed background subagents directly inside an interactive TUI panel.

## Before you begin

*   [Install Antigravity CLI](/docs/cli/install)
*   Understand the [Asynchronous execution model](/docs/cli/subagents)

## Overview

The `/agents` command opens the interactive **Agent Manager Panel**. This interface serves two distinct purposes:

1.  **Custom Agent Selection & Discovery**: Choose between the default agent and custom workflow-specific agents, or discover where to define new agents locally and globally.
2.  **Subagent Monitoring & Control**: Track, inspect, or terminate background subagents running concurrently during your active session.

> **Note**: Subagent Specification:** For complete details on subagent lifecycle states, inter-agent communication, and custom Markdown agent specifications (`.md`), consult the [Antigravity 2.0 Subagents Documentation](/docs/subagents) and [CLI Subagents Guide](/docs/cli/subagents).

To open the panel inside the TUI, type `/agents` and press Enter:

```
/agents
```

![Interactive Agents Panel](/assets/image/docs/cli/agents-panel.png)

* * *

## Custom Agent Selection & Discovery

Antigravity CLI supports loading custom agent definitions with specialized system instructions and tool permissions. The **Available Agents** section lists all agents currently available to your session.

### 1\. Switching between agents

*   **Select**: Use ↑/↓ to highlight an agent (`Default agent` or a custom agent) under **Available Agents**, then press Enter.
*   **Status Indicator**: A green circle (`●`) indicates the active or prepared agent.
*   **Apply & Exit**: Press Esc to close the panel and apply your selection.

Note

If you are currently inside an active conversation, switching custom agents automatically forks your current session (`[ Switch will fork the current conversation on exit ]`) so you do not lose context. If you start from a fresh session, the switch applies directly (`[ Switch will create a new conversation on exit ]`).

### 2\. Creating custom agents

The header of the `/agents` panel displays exact template locations for creating new custom agents:

```
Create New Agents
  Workspace: {workspace}/.agents/agents/{agent_name}/agent.md
  Global: ~/.gemini/config/agents/{agent_name}/agent.md
```

To create a custom agent that is available across all your workspaces and projects, place it under your global customization directory (`~/.gemini/config/agents/`). Create a directory matching your agent name and add an `agent.md` file with YAML frontmatter:

```
mkdir -p ~/.gemini/config/agents/code-reviewer
cat << 'EOF' > ~/.gemini/config/agents/code-reviewer/agent.md
---
name: code-reviewer
description: Rigorous code review specialist focusing on edge cases and security.
---
You are an expert code reviewer. Analyze diffs carefully and verify edge cases.
EOF
```

When you reopen `/agents`, the CLI automatically discovers `code-reviewer` and lists it under **Available Agents**. If you need an agent scoped strictly to a single project repository, place it inside that workspace’s `.agents/agents/` directory (for example, `/home/user/projects/my-app/.agents/agents/code-reviewer/agent.md`). You can also package and distribute custom agents inside [Plugins](/docs/cli/plugins).

* * *

## Subagent Monitoring & Control

When your primary agent delegates tasks (such as running tests or querying large codebases), the spawned threads appear in the `/agents` panel under **Subagents**, grouped by their triggering prompt.

### 1\. Inspecting subagent progress

*   **Group Toggling**: Press Enter on a subagent group header (`▸ Subagents (1 running, 2 done)`) to expand or collapse (`▾`) that group.
*   **Status Indicators**: Each subagent row displays a live lifecycle state:
    *   `running`: Actively executing tools or generating reasoning steps.
    *   `done`: Successfully completed its assigned background task.
    *   `error`: Encountered a terminal failure during execution.
    *   `killed`: Terminated manually by the user or parent process.
*   **Detail View**: Highlight a specific subagent row and press Enter to open the full-screen **Subagent Detail View**. This view displays the subagent’s complete internal thoughts, tool calls, and execution stdout. Press Esc to return to the list.

### 2\. Terminating active subagents

If a background subagent loops or runs longer than needed, you can kill it immediately without leaving your session:

1.  Open `/agents` and highlight the running subagent row.
2.  Press K to kill the active subagent and all its child threads.

### 3\. Inline tool approvals

If a subagent attempts a protected operation (such as modifying a file or running a shell command in a sandboxed environment), the authorization prompt displays inline in the `/agents` panel. You can press A to approve or D to deny directly from the list.

* * *

## Panel Keybindings Reference

When focused inside the `/agents` panel, the following keyboard shortcuts apply:

| Key | Action | Behavior |
| :-- | :-- | :-- |
| ↑ / ↓ | Navigate | Move the cursor between headers, subagents, and available agents. |
| Enter | Select / Toggle | Expand/collapse groups, open Subagent Detail View, or select a custom agent. |
| K | Kill Active Subagent | Instantly cancel (`CancelSubagent`) the highlighted running subagent. |
| Esc | Go Back | Exit the panel, return to the prompt box, and apply any prepared agent switch. |

* * *

## Common mistakes

| Mistake | Why it fails | Fix |
| :-- | :-- | :-- |
| Expecting custom agent switches to modify turn history | Switching agents forks the conversation to preserve historical integrity | Continue your workflow in the newly forked session |
| Placing agent files directly in config root | Scanner looks specifically inside `agents/` directories | Move definition to `.agents/agents/<name>/agent.md` |
| Pressing K on completed subagents | Only targets active (`running`) subagent processes | Press Enter to inspect completed logs instead |

* * *

## Next steps

*   [Background tasks & subagents](/docs/cli/subagents): Learn more about the multi-threaded asynchronous execution architecture.
*   [Plugins & Skills](/docs/cli/plugins): Discover how to bundle custom agents, skills, and MCP configs into shareable plugins.
*   [Permissions & Sandbox](/docs/cli/sandbox): Configure security guardrails and approval rules for background subagents.

# Code Search Command (/codesearch)

Interactively search the code in your workspace from inside the TUI, without leaving your session or interrupting the agent.

## Overview

The `/codesearch` command opens a fullscreen **Code Search** panel that runs a search across your current workspace and shows the matches grouped by file, with surrounding context and the matched text highlighted. It is handy for quickly locating a symbol, string, or pattern and then jumping straight to the file at the matching line. `/codesearch` directly queries your workspace and returns results instantly.

The command has two aliases: `/cs` and `/search`.

## Running a search

1.  Type `/codesearch` followed by your query in the prompt box.
2.  Press Enter.

```
/codesearch UserSession
```

The Code Search panel opens with the results grouped by file. The header shows your query and the number of matches, and each match is displayed with one line of context above and below. The matched text is highlighted:

![The Code Search panel showing matches for a query grouped by file with highlighted results](/assets/image/docs/cli/codesearch-results.png)

### Navigation and controls

The panel is fully keyboard driven:

| Key | Action |
| :-- | :-- |
| ↑ / ↓ | Move between individual matches |
| ← / → | Jump to the previous / next file group |
| Enter | Open the highlighted result in the file viewer at the matching line |
| Ctrl + G | Open the highlighted result in your external editor at the matching line |
| Esc | Close the panel and return to the prompt |

## Query syntax

By default, queries are interpreted as **regular expressions** and matching is case-insensitive unless your query contains an uppercase letter (smart case).

### Literal (fixed-string) matching

Add `-F` (or `--literal`) anywhere in the query to disable regex and match the text literally. This is useful when your query contains regex metacharacters such as `.`, `(`, or `*`:

```
/codesearch -F map[string]*UserSession
```

### Filtering by file path

Restrict a search to certain files with `f:` (aliases `file:` and `path:`) followed by a glob. Prefix the filter with `-` to _exclude_ matching files instead:

```
/codesearch f:store.go Session
```

```
/codesearch -f:*_test.go NewUserSession
```

![The Code Search panel scoped to a single file using an f: path filter](/assets/image/docs/cli/codesearch-filter.png)

## Opening a file and commenting on lines

Code Search is more than a viewer — you can open any result and give the agent precise, line-level feedback without leaving the CLI.

### Open a result

Highlight a match with ↑ / ↓ and press Enter to open that file in the built-in file viewer, scrolled to the matching line. Use Ctrl + G instead to open it in your external editor.

Inside the file viewer, the footer shows the available actions:

```
↑/↓ scroll · pgup/pgdown page · shift+g bottom · g top · c comment · ctrl+g editor · / search
```

### Comment on a specific line

1.  Move the cursor (↑ / ↓) to the line you want to annotate.
2.  Press C to open the inline comment editor for that line.
3.  Type your note. Use Shift + Enter (or Alt + Enter) for a new line, and press Enter to save it.

A saved comment is stored against that line and marked with a 💬 icon in the gutter. Repeat for as many lines as you like. To remove a comment, place the cursor on the line and press the delete key (D).

![Leaving a line comment in the file viewer opened from Code Search](/assets/image/docs/cli/codesearch-comment.png)

### Send your comments to the agent

When you leave the file viewer with Esc, any pending comments are collected and the CLI asks whether to send them:

*   Y — **send + close**: your comments are delivered to the agent as your next message, formatted as `<file>:<line>: <comment>` so the model knows exactly which lines you mean.
*   N — **discard + close**: exit without sending.
*   Esc — cancel and keep editing.

![Confirming whether to send unsent line comments to the agent](/assets/image/docs/cli/codesearch-comment-send.png)

This makes Code Search a fast way to find relevant code and hand the agent targeted, line-anchored instructions in a single flow.

## Next steps

*   **[CLI Features](/docs/cli/features)**: Explore the rest of the interactive TUI capabilities.
*   **[Prompting Guide](/docs/cli/prompting)**: Learn how to direct the agent to search and edit code for you.
*   **[Resume Command (/resume)](/docs/cli/commands/resume)**: Navigate and manage your past conversations.

# AI Credits Command (/credits)

View and manage your AI Premium credits interactively.

## Overview

The `/credits` command opens a dedicated panel in the TUI that displays your current AI Premium credit balance, consumption history, and links to manage your subscription or purchase additional credits.

For details on how credits are tracked, low credit alerts, and settings configuration, see the conceptual **[AI Credits Guide](/docs/cli/credits)**.

## Using the Credits Command

To view your credit status:

1.  Type `/credits` in the prompt box.
2.  Press `Enter`.

```
/credits
```

The credits panel will display:

*   **Active Balance**: Your remaining AI Premium credits.
*   **Usage Summary**: A breakdown of credits consumed in the current billing cycle.
*   **Quick Links**: Actions to buy more credits or upgrade your plan (which will open the relevant web portals).

Press `Esc` to close the panel and return to the main prompt.

## Next steps

*   **[AI Credits Guide](/docs/cli/credits)**: Learn about credit consumption, alerts, and settings.
*   **[Model Quotas Command](/docs/cli/commands/usage)**: Monitor your model-specific API quotas.
*   **[CLI Reference](/docs/cli/reference)**: See all available slash commands.

# Diff Command (/diff)

View and review workspace changes, commit history, and agent turn diffs interactively within the TUI.

## Overview

The `/diff` command opens the **Interactive Diff Viewer**, a full-screen panel that allows you to inspect changes in your workspace and conversation history. It supports three distinct modes (VCS, Turn, and Commit) and provides an interactive review workflow where you can add line-by-line comments to steer the agent’s next steps.

## Interactive Diff Viewer Panels

To open the Diff Viewer:

1.  Type `/diff` in the prompt box.
2.  Press Enter.

```
/diff
```

### Navigation and Controls

The Diff Viewer operates in three modes, which you can cycle through using Tab (or → / ← arrow keys):

*   **VCS Mode**: Shows a list of all modified and untracked files in your active workspace.
    *   Supports Git, Mercurial (Hg), and Jujutsu (JJ) automatically.
    *   Use ↑/↓ to navigate the file list, and Enter to open the detail view.
*   **Turn Mode**: Shows the changes introduced by the agent in each turn of the current conversation.
    *   Useful for reviewing the agent’s work step-by-step.
    *   Use ↑/↓ to navigate, and Enter to view details.
*   **Commit Mode**: Renders an interactive commit graph/tree of your repository.
    *   Use ↑/↓ to navigate the commit chain.
    *   Use ←/→ to navigate to adjacent branches in the graph.
    *   Press Enter to load the diff for the selected commit.

* * *

## Step-by-Step Walkthrough

Here is how to use the Diff Viewer to review changes, add comments, and steer the agent.

### 1\. Reviewing Workspace Changes (VCS Mode)

When you run `/diff`, it opens in **VCS Mode** by default (if you have uncommitted changes). You will see a list of modified and untracked files:

![VCS Diff List](/assets/image/docs/cli/diff-vcs-list.png)

Press Enter on a file to open its **Detail View**. This shows the unified diff.

*   Use ↑/↓ (arrow keys) to scroll the diff.
*   Use J/K (or ←/→) to quickly swap between files without returning to the list.
*   Use N/Shift + N to jump to the next/previous diff hunk.

![Detail View](/assets/image/docs/cli/diff-detail.png)

### 2\. Adding Comments and Steering the Agent

While in the Detail View, you can review the code and write feedback directly onto specific lines.

**Step 1: Locate the line**  
Scroll to the line you want to comment on.

**Step 2: Open the comment input**  
Press C. The **Comment Input** overlay opens at the bottom:

![Comment Input](/assets/image/docs/cli/diff-comment.png)

**Step 3: Write your feedback**  
Type your feedback and press Enter to save (or Esc to cancel).

**Step 4: Manage your comments**  
Saved comments are marked in the diff. You can delete a comment by highlighting the line and pressing D.

**Step 5: Exit and submit**  
Press Esc to return to the file list. Press Esc again to exit `/diff`. If you have unsaved comments, a confirmation screen appears:

*   Press Shift + Y to approve and exit. Your comments are formatted and sent to the agent as your next prompt, allowing you to steer its next turn.
*   Press Shift + N to reject and exit, discarding the comments.

### 3\. Reviewing Turn History (Turn Mode)

Press Tab to switch to **Turn Mode**. This groups changes by the conversation turn in which they were introduced, allowing you to see exactly what the agent did in previous steps:

![Turn Diff List](/assets/image/docs/cli/diff-turn-list.png)

### 4\. Navigating the Commit Tree (Commit Mode)

Press Tab again to switch to **Commit Mode**. This renders the repository’s commit history as an interactive graph. You can navigate up and down the chain, or hop between branches using ←/→:

![Commit List](/assets/image/docs/cli/diff-commit-list.png)

Highlight any commit and press Enter to load and review its diff:

![Commit Detail](/assets/image/docs/cli/diff-commit-detail.png)

* * *

## Keyboard Shortcuts Reference

### File List View (VCS & Turn Modes)

| Key | Action |
| :-- | :-- |
| Tab / → / ← | Cycle modes (VCS → Turn → Commit) |
| ↑ / ↓ (or J / K) | Navigate file list |
| Enter | Open selected file’s Detail View |
| Esc | Exit Diff Viewer |

### File Detail View

| Key | Action |
| :-- | :-- |
| ↑ / ↓ | Scroll diff content |
| PgUp / PgDn | Scroll diff by page |
| J / K (or → / ←) | Switch to next / previous file |
| N / Shift + N | Jump to next / previous diff hunk |
| C | Add/edit comment on the current line |
| D | Delete comment on the current line |
| Esc | Return to File List View |

### Commit Tree View (Commit Mode)

| Key | Action |
| :-- | :-- |
| ↑ / ↓ | Navigate commit history |
| ← / → | Navigate to adjacent branches in the graph |
| Enter | Load diff for the selected commit |
| Esc | Exit Diff Viewer |

### Exit Confirmation Screen

| Key | Action |
| :-- | :-- |
| Shift + Y | Exit and send comments to the agent |
| Shift + N | Exit and discard comments |
| Esc | Return to File List View |

## See also

*   **[Settings & Keybindings](/docs/cli/settings)**: Customize your TUI theme, alt-screen preferences, and keybindings.
*   **[Conversations](/docs/cli/conversations)**: Learn how to manage, fork, and rewind conversation threads.
*   **[CLI Reference](/docs/cli/reference)**: Quick reference for all slash commands and default shortcuts.

# Permissions Command (/permissions)

Manage your fine-grained agent permission rules interactively within the TUI.

## Overview

Antigravity CLI uses a fine-grained permissions engine to secure your workstation. While you can configure these rules manually in your settings file, the `/permissions` command opens an interactive **Permissions Manager** TUI panel to view, add, edit, and delete rules live.

For details on how the permission engine works, supported actions, and manual configuration, see the conceptual **[Permissions Guide](/docs/cli/permissions)**.

## Managing permissions interactively

To open the Permissions Manager:

1.  Type `/permissions` in the prompt box.
2.  Press Enter.

```
/permissions
```

### Navigation and controls

The Permissions Manager operates in three panels:

1.  **Scope Picker**: Select the configuration scope you want to edit:
    
    *   **Project**: Rules applying only to the active project (disabled if no project is open).
    *   **Shared**: Rules shared across all Antigravity products.
    *   **Global**: Global rules applying to all your sessions.
    
    Use ↑/↓ (or J/K) to navigate, Enter to select, and Esc to exit.
    
2.  **Rule Viewer**: View the rules configured for the selected scope.
    
    *   Switch between **allowlist**, **denylist**, and **asklist** tabs using ←/→ (or Tab).
    *   Scroll through the rules using ↑/↓ (or J/K).
    *   Press A to add a new rule.
    *   Press E (or Ctrl + G) to edit the highlighted rule.
    *   Press D (or Backspace) to delete the highlighted rule.
    *   Press Esc to return to the Scope Picker.
3.  **Add/Edit Rule**: Type or edit a rule in the input field.
    
    *   Rules must follow the `action(target)` format (e.g., `command(git)`).
    *   Press Enter to validate and save the rule.
    *   Press Esc to cancel.

* * *

## Step-by-step walkthrough

Here is how to view, add, edit, and delete rules live in the TUI.

### 1\. Selecting a scope and viewing rules

When you run `/permissions`, you first see the **Scope Picker**. Select **Global** to manage your global rules:

![Selecting Global Scope](/assets/image/docs/cli/permissions-scope.png)

Press Enter to open the **Rule Viewer** for the selected scope. You can use ←/→ to switch between the **allow**, **deny**, and **ask** tabs:

![Global Rule Viewer](/assets/image/docs/cli/permissions-viewer.png)

### 2\. Adding a permission rule

To allow the agent to run `git` commands automatically without prompting:

1.  In the Rule Viewer, press A. The **Add Rule** panel opens at the bottom:
    
    ![Add Rule Panel](/assets/image/docs/cli/permissions-add.png)
    
2.  Type `command(git)` in the input field:
    
    ![Typing the Rule](/assets/image/docs/cli/permissions-add-typed.png)
    
3.  Press Enter. The rule is validated and saved. You are returned to the Rule Viewer, and `command(git)` now appears in your allowlist:
    
    ![Rule Saved Successfully](/assets/image/docs/cli/permissions-viewer-with-rule.png)
    

### 3\. Editing a permission rule

If you want to restrict the agent so it can only run `git diff` automatically, you can edit the rule:

1.  In the Rule Viewer, use ↑/↓ to highlight `command(git)`.
2.  Press E (or Ctrl + G). The input panel opens, prefilled with `command(git)`.
3.  Modify the text to `command(git diff)`.
4.  Press Enter to save. The old rule is replaced by the new one.

### 4\. Deleting a permission rule

To remove a rule and revert to prompting for those actions:

1.  In the Rule Viewer, highlight the rule you want to delete (e.g., `command(git diff)`).
2.  Press D (or Backspace).
3.  The rule is immediately removed from the list.

## Next steps

*   **[Permissions Guide](/docs/cli/permissions)**: Learn about the security model, action types, and wildcard matching.
*   **[Sandbox & Security](/docs/cli/sandbox)**: Configure the native OS container for running commands.
*   **[CLI Reference](/docs/cli/reference)**: See all available slash commands and keybindings.

# Resume Command (/resume)

Browse, search, and resume past conversation threads, or recover your last session instantly from the command line.

## Overview

Antigravity CLI allows you to maintain multiple ongoing development threads. The `/resume` command opens an interactive **Session Picker** TUI panel to browse and load your history. You can also resume sessions directly from your host terminal using command-line flags.

* * *

## Interactive Session Picker

To open the Session Picker inside the TUI:

1.  Type `/resume` (or aliases `/switch`, `/conversation`) in the prompt box.
2.  Press Enter.

```
/resume
```

### 1\. Navigating and Searching Conversations

The Session Picker displays a list of past conversations sorted by recency (newest first).

*   **Search**: Start typing to instantly filter conversations by their title, preview text, or unique ID.
*   **Navigate**: Use ↑/↓ to scroll through the filtered list.
*   **Page**: Use ←/→ to page backward and forward through older history blocks.
*   **Select**: Highlight your target session and press Enter to load it.
*   **Exit**: Press Esc to close the picker and return to the active prompt.

![Navigating Conversations](/assets/image/docs/cli/resume-navigate.png)

### 2\. Renaming a Conversation

To keep your history organized, you can rename conversations directly within the picker:

1.  Use ↑/↓ to highlight the conversation you want to rename.
2.  Press F2. An input field opens at the bottom of the panel, prefilled with the current title.
3.  Type the new name and press Enter to save, or Esc to cancel.

![Renaming a Conversation](/assets/image/docs/cli/resume-rename.png)

### 3\. Deleting a Conversation

To clean up obsolete threads:

1.  Highlight the target conversation in the list.
2.  Press Ctrl + Delete. A confirmation prompt appears.
3.  Press Enter (or Y) to confirm deletion, or Esc (or N) to cancel.

![Deleting a Conversation](/assets/image/docs/cli/resume-delete.png)

### 4\. Importing from Antigravity 2.0

You can import and resume active threads initiated in the Antigravity 2.0 desktop application:

1.  With the Session Picker open, press Tab to switch from the **CLI** tab to the **Antigravity** tab.
2.  Highlight the desktop conversation you wish to import.
3.  Press Enter. A confirmation prompt `[Import this? (y/n)]` appears.
4.  Press Enter (or Y) to confirm. The CLI clones the history, context, and tool trajectories into your terminal session.

![Importing from Antigravity 2.0](/assets/image/docs/cli/resume-antigravity.png)

* * *

## Command-Line Shortcuts

You can bypass the TUI picker and resume sessions directly when launching `agy` from your host shell.

### Quick Resume Last Session (`-c` / `--continue`)

To instantly resume the single most recent conversation associated with your active workspace:

```
agy -c
```

_(Alternative: `agy --continue`)_

### Resume Specific Session (`--conversation`)

To load a specific conversation directly by its unique ID:

```
agy --conversation <conversation-id>
```

* * *

## Under the Hood: The Session Cache

When you use the `-c` / `--continue` flag, the CLI resolves the target session using a local workspace-keyed cache.

### The Cache File

*   **Location**: `~/.gemini/antigravity-cli/cache/last_conversations.json`
*   **Format**: A JSON map associating absolute workspace directory paths with their most recently active conversation ID:
    
    ```
    {
        "/usr/local/google/home/username/Develop/my-project": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "/usr/local/google/home/username/Develop/another-repo": "f9e8d7c6-b5a4-3210-fedc-ba9876543210"
    }
    ```
    

### Resolution Workflow

1.  **Launch**: You run `agy -c` from `/path/to/workspace`.
2.  **Lookup**: The CLI reads `last_conversations.json` and looks up the key `/path/to/workspace`.
3.  **Verification**: If an ID is found, the CLI queries the backend to verify the conversation still exists.
4.  **Load**:
    *   If verified, it loads the session.
    *   If the conversation was deleted or the key is missing, it starts a fresh session for that workspace.

* * *

## See also

*   **[Managing Conversations](/docs/cli/conversations)**: Learn about workspace scoping and branching with `/fork`.
*   **[CLI Reference](/docs/cli/reference)**: See all available slash commands and default keybindings.
*   **[Settings & Keybindings](/docs/cli/settings)**: Configure rendering modes and customize keyboard shortcuts.

# Status Line Command (/statusline)

Toggle the TUI status line or configure a custom rendering command.

## Overview

The `/statusline` command allows you to quickly enable or disable the status line at the bottom of your TUI, or configure a custom shell command to render it dynamically, without manually editing your settings file.

For details on how to write custom status line scripts and the JSON state payload schema, see the conceptual **[Status Line Customization Guide](/docs/cli/statusline)**.

## Usage

Run the `/statusline` command with the following arguments to control its behavior:

### Toggle Status Line

Type `/statusline` with no arguments to toggle the status line on and off:

```
/statusline
```

### Enable or Disable Explicitly

You can explicitly enable or disable the status line:

*   **Enable**: `/statusline on` or `/statusline enable`
*   **Disable**: `/statusline off` or `/statusline disable`

```
/statusline off
```

### Configure a Custom Command

To route the agent state JSON payload to a custom script and render its output in the status line, pass the command as an argument:

```
/statusline ~/.gemini/antigravity-cli/statusline.sh
```

This immediately updates your settings and starts running the script to render the status line.

### Revert to Default

To delete your custom command configuration and revert to the built-in default status line:

```
/statusline delete
```

_(Note: `/statusline reset` is also supported)._

### Show Help

To view the quick command reference:

```
/statusline help
```

## Next steps

*   **[Status Line Guide](/docs/cli/statusline)**: Learn how to write custom scripts and handle the JSON payload.
*   **[Window Title Command](/docs/cli/commands/title)**: Configure dynamic terminal window titles.
*   **[CLI Reference](/docs/cli/reference)**: See all available slash commands.

# Window Title Command (/title)

Configure dynamic terminal window titles interactively.

## Overview

The `/title` command allows you to toggle the terminal window title feature on and off, or set its state explicitly. When enabled, the terminal title bar dynamically updates to show the active model, workspace, and agent state.

For details on how to write custom scripts to format the window title, see the conceptual **[Terminal Title Customization Guide](/docs/cli/title)**.

## Interactive Toggling

You can control the window title feature by running the `/title` command.

To toggle the feature on and off:

```
/title
```

To enable it explicitly:

```
/title on
```

To disable it explicitly:

```
/title off
```

## Next steps

*   **[Terminal Title Guide](/docs/cli/title)**: Learn how to write custom scripts to format the window title.
*   **[Status Line Command](/docs/cli/commands/statusline)**: Customize your TUI status line.
*   **[CLI Reference](/docs/cli/reference)**: See all available slash commands.

# Model Quotas (/usage)

View your active model quota usage and refresh your configuration.

## Overview

Antigravity CLI provides the `/usage` command (alias `/quota`) to help you monitor your resource consumption. When run, the command refreshes your model configuration and quota status from the backend and opens an interactive TUI panel.

## Viewing your usage

To open the Model Quotas panel:

1.  Type `/usage` (or `/quota`) in the prompt box.
2.  Press Enter.

```
/usage
```

![Quota & Credits TUI](/assets/image/docs/cli/usage-tui.png)

### Interactive Panel Features

The panel displays:

*   **Model Quotas**: A breakdown of your usage limits and remaining requests/tokens for each supported model (e.g., Gemini 3.5 Flash, Gemini 3.1 Pro).
*   **Active Refresh**: The CLI automatically triggers a fresh check of your quotas on disk and from the backend service when you open this panel.

### Navigation Controls

Use the following keyboard shortcuts to navigate the panel:

| Key | Action |
| :-- | :-- |
| ↑ / ↓ (or J / K) | Scroll up or down by one line. |
| PgUp / PgDn | Scroll up or down by one page. |
| G / Shift + G | Jump to the top or bottom of the list. |
| Esc (or Q) | Close the panel and return to the prompt. |

## Next steps

*   **[CLI Reference](/docs/cli/reference)**: See all available slash commands and keybindings.
*   **[Settings & Rendering](/docs/cli/settings)**: Configure your default models and credit usage preferences.

# Best practices for Antigravity CLI

Master the workflows, prompt architectures, and local configuration choices to maximize agent velocity while maintaining robust control.

## Establish verification loops

The single most effective way to ensure reliable, correct modifications from an autonomous agent is to provide the agent with a local verification mechanism (such as unit tests, build commands, or formatting scripts).

Before asking the agent to implement a code change:

1.  Ensure your workspace directory has a test suite ready.
2.  If tests do not exist, direct the agent to write a standard test block _first_.
3.  Once the agent proposes code, instruct it to run the local test command to verify its work.
4.  Watch the agent execute the command and iterate on the test outputs automatically.

```
> Implement feature X in main.py. Run npm test afterward to verify the build.
```

## Explore, plan, then execute

Autonomous local agents operate with highest accuracy when complex changes are partitioned into distinct exploration, planning, and execution phases.

*   **Exploration**: Ask the agent to explain how the target codebase resolves a particular problem or where an interface is defined before writing any changes.
*   **Planning**: Request an implementation plan. The agent will list targeted files, required dependencies, and logic overrides in an implementation plan artifact.
*   **Execution**: Once you approve the structured plan, direct the agent to apply the edits.

```
> Explore how our router resolves `/docs/:page`. Write down an implementation plan to add `/docs/best-practices`.
```

## Enrich your prompting context

Give local agents high-fidelity indicators to narrow down reasoning boundaries and minimize token overhead.

### Target file autocompletion

Type `@` within your prompt box to trigger the **Interactive Path Suggestion** overlay. Highlighting and selecting a path imports the absolute workspace file path directly into your prompt. This helps the agent target its code searches.

### Attaching visual evidence

If debugging visual UI issues, rendering bugs, or frontend layout inconsistencies, capture a screenshot or video recording, copy it, and press `ctrl+v` inside the prompt box to attach it. The agent will consult the media file to diagnose the issue.

## Configure your workspace environment

Optimize your local workstation rules and security boundaries to match your engineering flow.

### Write a codebase rule file

Create a `GEMINI.md` or `AGENTS.md` file at your workspace root to outline specific directory standards, styling paradigms, test command parameters, and deprecation warnings. The agent automatically parses these rules on startup and consults them before suggesting changes.

### Establish structured permissions

Tune your safety barriers in `~/.gemini/antigravity-cli/settings.json` based on your project risk level:

*   **`request-review`** (Default): Prompts you before executing any write operations, bash commands, or remote network calls.
*   **`proceed-in-sandbox`**: Restricts all terminal executions to a secure sandbox containment ring. Safe commands execute autonomously, while risky commands prompt for reviews.
*   **`strict`**: Always prompts for all non-read operations, providing complete line-by-line transparency.

```
{
    "toolPermission": "proceed-in-sandbox",
    "enableTerminalSandbox": true
}
```

## Manage TUI sessions proactively

Use active session navigation tools to recover from engineering dead-ends or course-correct intermediate agent loops.

### Course-correct early (`esc`)

If you watch an agent execute an incorrect search pattern or write code that deviates from your intentions, press the global escape hatch key `esc` immediately to interrupt the turn and regain focus of a clean prompt.

### Rewind history with `/rewind`

If an agent has made several successive changes that introduce build errors, you do not need to discard the session. Type `/rewind` (or `/undo`) to roll back your conversation thread to a previous stable checkout.

### Branch experiments with `/fork`

If you are unsure of the best implementation path:

1.  Reach a stable baseline thread.
2.  Type `/fork` to spin up a duplicate parallel session.
3.  Test your speculative code modifications in the branched session.
4.  If the approach fails, run `/resume` to swap back to your stable main branch.

## Automate and script

Antigravity CLI is designed to operate seamlessly within standard shell pipeline tools.

### Run non-interactive commands (`-p`)

To automate quick queries or integrate agents into git hooks, use the one-shot prompt flag `-p`:

```
agy -p "Review this git diff and draft a conventional commit message" --cwd $(pwd)
```

### Fan out using parallel subagents

For large-scale sweeps or multi-file refactoring, direct the primary agent to spawn concurrent background subagents. The agent manager handles background threads autonomously while you continue working on your primary screen.

## Related resources

Learn how to configure settings and customize visual layouts:

*   **[Settings, Rendering & Keybindings](/docs/cli/settings)**: Customize keyboard hotkeys and buffers.
*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Enforce filesystem containment.
*   **[Plugins & Skills](/docs/cli/plugins)**: Create your own custom slash commands.

# Troubleshooting

Diagnose and resolve common anomalies with installation PATHs, local self-updating locks, keyring access permissions, and SSH clipboard forwarding.

## Quick reference

Scan the lookup table below to identify symptoms and access immediate solutions:

| Error Symptom | Potential Cause | Target Resolution |
| :-- | :-- | :-- |
| **`agy: command not found`** | Binary directory missing from shell environments. | [Configure your shell PATH](#configure-your-shell-path) |
| **`keyring: secure lock out`** | Missing system service permissions or active lockouts. | [Authorize keyring permissions](#authorize-keyring-permissions) |
| **`SSH Clipboard paste failures`** | Protocol streams blocked or missing forward configurations. | [Enable emulator clipboard forwarding](#enable-emulator-clipboard-forwarding) |
| **`Advisory lock / update failures`** | Locked self-updater thread or read-only directory paths. | [Resolve self-updater locks and failures](#resolve-self-updater-locks-and-failures) |

* * *

## Configure your shell PATH

### Symptom

Executing `agy` returns a shell terminal error:

```
bash: agy: command not found
```

### Cause

The installation utility downloads the binary to `~/.local/bin` (or `C:\Users\<username>\AppData\Local\agy\bin`), but your shell’s active `$PATH` environment does not index this directory.

### Resolution

Ensure your terminal session loads the binary path.

**macOS & Linux**:

1.  Open your shell configuration file (`~/.bashrc` or `~/.zshrc`).
2.  Verify or append the following line at the end of the file:
    
    ```
    export PATH="~/.local/bin:$PATH"
    ```
    
3.  Reload your profile configurations:
    
    ```
    source ~/.zshrc
    ```
    

**Windows (PowerShell)**:

1.  Open a PowerShell terminal as an Administrator and execute:
    
    ```
    [System.Environment]::SetEnvironmentVariable("Path", [System.Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Program Files\Google\antigravity-cli", "User")
    ```
    
2.  Restart your terminal emulator for the system registry environment to refresh.

* * *

## Authorize keyring permissions

### Symptom

When launching, the CLI hangs, prints DBUS warnings, or throws keyring access exceptions:

```
Error: failed to retrieve token: secret keyring is locked
```

### Cause

Antigravity CLI utilizes secure keychain libraries (Apple Keychain, Linux secret-service via dbus, or Windows Credential Manager) to encrypt your session tokens. If the background daemon is locked or headless, the CLI cannot read credentials.

### Resolution

**macOS**:

1.  Open **Keychain Access** app.
2.  Search for the `Antigravity CLI` security item.
3.  Right-click, select **Get Info**, choose the **Access Control** tab, and verify that `agy` is on the allowed applications list.
4.  If running inside a headless SSH session on Mac, run the following unlock sequence:
    
    ```
    security unlock-keychain -p "your_keychain_password" login.keychain
    ```
    

**Linux**:

Ensure your system keyring (such as GNOME Keyring or KWallet) is unlocked and accessible.

If you are running in a headless environment or over SSH, ensure that a D-Bus session is active and that your keyring daemon is running. You can typically initialize a D-Bus session by running:

```
export $(dbus-launch)
```

If you still experience access issues, ensure your user account has the necessary permissions to access the keyring service or reach out to support.

* * *

## Enable emulator clipboard forwarding

### Symptom

Pasting screenshots or media files via `Ctrl+V` within an SSH terminal returns a failure notification:

```
Error: local pasteboard is empty or unreachable over SSH connection
```

### Cause

Standard SSH streams do not forward graphical clipboards. Graphic uploads require specific terminal multiplexer protocols.

### Resolution

Verify that you are utilizing supported terminal emulators and configurations.

1.  **Use iTerm2 or Ghostty**: These emulators support advanced clip channels.
2.  **Configure iTerm2 Forwarding**:
    *   Open iTerm2 Preferences (`Cmd+,`).
    *   Go to the **General** tab, select **Selection** submenu.
    *   Check **Applications in terminal may access clipboard** (enabling OSC 52 write channels).
3.  **Bypass Multiplexers**: If running inside `tmux`, ensure your active configuration maps standard paste clips correctly:
    
    ```
    set -s set-clipboard on
    ```
    

* * *

## Resolve self-updater locks and failures

### Symptom

Launching `agy` hangs, fails to apply upgrades, or returns an advisory lock warning:

```
Warning: another background updater process is already active (update.lock)
```

### Cause

Antigravity CLI contains a native, statically linked self-updater that runs in the background. It uses a 15-minute Time-To-Live (TTL) debounce marker (`last_check.timestamp`) and an advisory lock (`update.lock`) inside `~/.gemini/antigravity-cli/updater/` to prevent concurrent process collisions. If a background updater process hangs, crashes without releasing the lock, or has insufficient user filesystem permissions inside the executable directory, subsequent updates are blocked.

### Resolution

*   **Release the advisory lock**: Purge the background lock file manually:
    
    ```
    rm -f ~/.gemini/antigravity-cli/updater/update.lock
    ```
    
*   **Opt-out/Disable auto-updates**: Set the `AGY_CLI_DISABLE_AUTO_UPDATE` environment variable to `true` inside your shell profile (`~/.bashrc` or `~/.zshrc`):
    
    ```
    export AGY_CLI_DISABLE_AUTO_UPDATE=true
    ```
    
*   **Verify directory write permissions**: Ensure your user profile owns and has write permissions inside the target installation directory (`~/.local/bin/` on Unix, or `%LOCALAPPDATA%\agy\bin` on Windows).

* * *

## Next steps

Access our quick reference sheets or configure advanced permissions:

*   **[CLI Reference](/docs/cli/reference)**: Dense tables listing all slash commands and visual settings keys.
*   **[Permissions](/docs/cli/permissions)**: Configure fine-grained allowed and denied action policies.
*   **[Sandbox](/docs/cli/sandbox)**: Enforce OS-level container isolation boundaries.
*   **[Plugins & Skills](/docs/cli/plugins)**: Create your own custom skills.

# CLI reference

Scan scannable tables listing all TUI slash commands, default keyboard shortcuts, and JSON configuration parameters.

## Core slash commands

Type `/` inside the prompt box to open the typeahead command selection menu.

| Command | Category | Alias | Execution Purpose |
| :-- | :-- | :-- | :-- |
| **`/add-dir <path>`** | Utilities | — | Add a directory path to the active workspace. |
| **[`/agents`](/docs/cli/commands/agents)** | Tools & Tasks | — | Open the [Agent Manager Panel](/docs/cli/commands/agents) to switch custom agents and monitor background subagents. |
| **`/artifact`** | Tools & Tasks | — | Open the Artifact Review Panel. |
| **`/btw <query>`** | Utilities | — | Ask a side question in the background without interrupting the main conversation. |
| **`/clear`** | Utilities | `/new` | Clear the terminal and reset active conversation contexts. |
| **`/config`** | Configurations | `/settings` | Open the interactive Settings Editor Overlay. |
| **`/context`** | Utilities | — | Open the context usage visualization panel. |
| **`/copy`** | Utilities | — | Copy the last agent response to the system clipboard. |
| **[`/credits`](/docs/cli/commands/credits)** | Account | — | View remaining G1 credits and purchase links. |
| **[`/diff`](/docs/cli/commands/diff)** | Utilities | — | Open the [Interactive Diff Viewer](/docs/cli/commands/diff) to view changes, turns, and commits. |
| **`/exit`** | Core | `/quit` | Close the TUI session and restore your host shell. |
| **`/fast`** | Configurations | — | Enable fast mode (bypass reasoning plans) for quick actions. |
| **`/feedback`** | Utilities | — | Open the feedback submission panel. |
| **`/fork`** | Conversations | `/branch` | Clone the current conversation thread into a new parallel session. |
| **`/help`** | Utilities | — | Open the help panel showing commands and shortcuts. |
| **`/hooks`** | Tools & Tasks | — | Browse active pre-flight/post-format script hooks. |
| **`/keybindings`** | Configurations | — | Open the interactive Keyboard Shortcut Editor. |
| **`/logout`** | Account | — | Disconnect your profile and purge authentication tokens from the secure keyring. |
| **`/mcp`** | Tools & Tasks | — | Open the Model Context Protocol (MCP) server manager. |
| **`/model`** | Configurations | — | Choose your preferred reasoning model (persists across sessions). |
| **`/open <path>`** | Utilities | — | Force the path to open inside your default system editor. |
| **[`/permissions`](/docs/cli/commands/permissions)** | Configurations | — | Open the interactive tool permissions manager panel. |
| **`/planning`** | Configurations | — | Enable multi-turn plan generation mode for complex engineering tasks. |
| **`/rename <name>`** | Conversations | — | Rename the current session thread. |
| **[`/resume`](/docs/cli/commands/resume)** | Conversations | `/switch`, `/conversation` | Open the [conversation picker overlay](/docs/cli/commands/resume) to select and load previous threads. |
| **`/rewind`** | Conversations | `/undo` | Roll back your conversation history to a previous message. |
| **`/skills`** | Tools & Tasks | — | Browse loaded local and global Agent Skills. |
| **[`/statusline`](/docs/cli/commands/statusline)** | Configurations | — | Open the Status Bar customization overlay. |
| **`/tasks`** | Tools & Tasks | — | Open the Task Manager Panel to monitor background shell execution logs. |
| **[`/title`](/docs/cli/commands/title) \[on/off\]** | Configurations | — | Toggle or set terminal window title updates. |
| **[`/usage`](/docs/cli/commands/usage)** | Utilities | `/quota` | Display model quota usage. |

## Default keybindings

Keyboard shortcut commands mapping global, prompt, navigation, and approval operations.

### Global controls

These hotkeys are always active regardless of which panel, overlay, or prompt is currently focused.

| Key | TUI Command | Action Behavior |
| :-- | :-- | :-- |
| **`Esc`** | `cli.escape` | Closes active panels, halts active streams, or clears empty prompts. |
| **`Ctrl+C`** | `cli.exit` | Terminates the CLI session (prompts for confirmation if agent is working). |
| **`Ctrl+D`** | `cli.exit` | Exits the CLI session (only when the prompt box is empty). |
| **`Ctrl+L`** | `cli.clear_screen` | Refreshes and clears the visual terminal buffer. |

### Prompt focus keys

These keys are active when writing instructions inside the prompt box.

| Key | TUI Command | Action Behavior |
| :-- | :-- | :-- |
| **`Enter`** | `prompt.submit` | Submits your prompt or active menu selection to the agent. |
| **`Shift+Enter`** / **`Ctrl+J`** | `prompt.newline` | Inserts a clean newline without submitting. |
| **`Ctrl+V`** | `prompt.paste` | Pastes graphic media files or clipboard blocks into the prompt. |
| **`Ctrl+O`** | `prompt.toggle_trajectory` | Expands or collapses detailed tool reasoning outputs. |
| **`Ctrl+R`** | `prompt.open_review` | Opens the Artifact Review Panel. |
| **`Ctrl+G`** | `prompt.external_editor` | Launches your default `$EDITOR` shell to compose your prompt. |
| **`Alt+J`** | `prompt.teleport_agent` | Instantly switches focus to the next subagent awaiting confirmation. |
| **`Ctrl+K`** | `prompt.fast_approve` | Instantly approves the pending subagent action listed in the status alert. |
| **`Ctrl+A`** | `prompt.cursor_start` | Moves the prompt insertion cursor to the beginning of the line. |
| **`Ctrl+E`** | `prompt.cursor_end` | Moves the prompt insertion cursor to the end of the line. |
| **`Ctrl+Z`** | `prompt.undo_text` | Reverts the last edit. |
| **`Ctrl+Shift+Z`** | `prompt.redo_text` | Redoes the last undone text operation. |
| **`Ctrl+D`** | `—` | Forward delete (only when the prompt box is non-empty). |

### Navigation & scrolling

Used inside select panels, menus, and scrollable text boxes.

| Key | TUI Command | Action Behavior |
| :-- | :-- | :-- |
| **`↑`** / **`↓`** | `navigation.up` / `navigation.down` | Scrolls highlighted selections up or down by one item. |
| **`PgUp`** / **`Shift+↑`** | `navigation.page_up` | Scrolls the active text viewport up by one page block. |
| **`PgDn`** / **`Shift+↓`** | `navigation.page_down` | Scrolls the active text viewport down by one page block. |
| **`←`** / **`→`** | `navigation.left` / `navigation.right` | Swaps pages inside multipage structures (like the Session Picker). |
| **`Tab`** | `navigation.tab` | Confirms the highlighted slash-command autofill option. |

### Tool confirmations

Active during confirmation prompts.

| Key | TUI Command | Action Behavior |
| :-- | :-- | :-- |
| **`y`** | `confirm.yes` | Authorizes the proposed tool, command, or active artifact. |
| **`n`** | `confirm.no` | Rejects the proposed tool, command, or active artifact. |
| **`A`** | `—` | (Inside Review Panel) Approves all generated artifacts in one action (built-in shortcut). |

## Configuration keys (`settings.json`)

Primary settings key names, data types, system defaults, and expected parameters.

### Example `settings.json`

```
{
    "colorScheme": "tokyo night",
    "altScreenMode": "always",
    "toolPermission": "request-review",
    "notifications": true,
    "enableTerminalSandbox": true
}
```

| Option Key Name | Value Type | System Default | Parameter Characteristics & Options |
| :-- | :-- | :-- | :-- |
| **`colorScheme`** | string | `"terminal"` | Color theme: `"light"`, `"solarized light"`, `"colorblind-friendly light"`, `"dark"`, `"solarized dark"`, `"colorblind-friendly dark"`, `"tokyo night"`, or `"terminal"` (inherits native shell colors). |
| **`altScreenMode`** | string | `"default"` | Screen buffer usage: `"default"` (adaptive inline/altscreen), `"always"` (force alternate screen buffer), or `"never"` (force inline sequential output). |
| **`toolPermission`** | string | `"request-review"` | Global safety presets: `"request-review"` (prompts for write/bash/web tools), `"proceed-in-sandbox"` (auto-proceed inside sandbox), `"always-proceed"` (never prompts), or `"strict"` (prompts for all non-read tools). |
| **`artifactReviewPolicy`** | string | `"asks-for-review"` | Code review policy: `"asks-for-review"` (always prompts before writing code), `"agent-decides"` (prompts dynamically), or `"always-proceed"` (never prompts). |
| **`notifications`** | boolean | `false` | Emits system desktop and terminal bell chime notifications upon task completions. |
| **`showTips`** | boolean | `true` | Displays helpful agentic tips above the prompt panel during generation turns. |
| **`showFeedbackSurvey`** | boolean | `true` | Displays periodic quality feedback surveys upon active task completions. |
| **`editor`** | string | `"auto"` | Target text editor utility: `"auto"` (consults system `$EDITOR`), `"vim"`, `"emacs"`, or custom text labels. |
| **`editorMode`** | string | `"default"` | Prompt editing model: `"default"` (flat text editing) or `"vim"` (modal editing). Distinct from `editor`, which selects an external program. See [Vim Editor Mode](/docs/cli/vim-editor-mode). |
| **`vimInsertFirst`** | boolean | `false` | Starts Vim editing in Insert mode and makes a bare `Enter` submit. Requires `editorMode` set to `"vim"`. |
| **`allowNonWorkspaceAccess`** | boolean | `false` | Permits the agent’s file read and write tools to navigate outside recognized Git/workspace roots. |
| **`enableTerminalSandbox`** | boolean | `false` | Restricts all local execution commands launched by agents to OS containment rings. |
| **`useG1Credits`** | boolean | `false` | _External builds only._ Uses personal AI credits for model calls once plan quotas are exhausted. |
| **`enableTelemetry`** | boolean | `true` | Permits metric collection and crash log streaming to improve tool reliability. |
| **`verbosity`** | string | `"high"` | Visual verbosity level: `"high"` (renders full thoughts and tool outputs) or `"low"` (displays only minimal visual progress indicators). |
| **`runningLightSpeed`** | string | `"medium"` | Visual running light progress animation speed: `"fast"`, `"medium"`, `"slow"`, or `"off"`. |

## Next steps

Learn how to safely deploy permission policies, sandboxes, and customize plugins:

*   **[Permissions & Sandbox](/docs/cli/sandbox)**: Enforce command-line containment rules.
*   **[Plugins & Skills](/docs/cli/plugins)**: Create your own custom skills slash commands.
*   **[Installation & Auth](/docs/cli/install)**: Update your CLI install.