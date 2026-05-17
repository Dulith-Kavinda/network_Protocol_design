# Network Protocol Design

A comprehensive Python-based project for designing, implementing, and analyzing network routing protocols. This project provides educational implementations and comparative analysis of modern routing protocols including OSPF, BGP, RIP, IS-IS, and an experimental AOSPF protocol.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Protocols Implemented](#protocols-implemented)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

This project focuses on the implementation and comparative analysis of network routing protocols across various layers of the OSI model. It provides practical implementations, simulation tools, and analysis utilities for understanding how modern network communication protocols operate.

## ✨ Features

- **Multiple Protocol Implementations**
  - OSPF (Open Shortest Path First)
  - BGP (Border Gateway Protocol)
  - RIP (Routing Information Protocol)
  - IS-IS (Intermediate System to Intermediate System)
  - AOSPF (Experimental Protocol)

- **Comparative Analysis Tools**
  - Protocol performance comparison
  - Topology-based simulation
  - Network communication utilities

- **Protocol Analysis and Testing**
  - Detailed protocol simulations
  - Performance metrics
  - Educational resources

- **Extensible Architecture**
  - Modular protocol implementations
  - Easy to extend with new protocols
  - Reusable utility functions

## 📦 Prerequisites

- **Python:** 3.x or higher
- **Dependencies:**
  - `networkx` - For network graph operations
  - Standard Python libraries (sys, os, etc.)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Dulith-Kavinda/network_Protocol_design.git
cd network_Protocol_design
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install required packages:

```bash
pip install networkx
```

## 📁 Project Structure

```
network_Protocol_design/
│
├── README.md
├── requirements.txt
│
├── ASOPF/
│   ├── README.md
│   ├── main.py
│   ├── topology/
│   │   └── [topology files]
│   └── protocol_sim/
│       └── [protocol simulation files]
│
├── ASOPF_comparison_with_isis_ospf_BGP_RIP/
│   ├── README.md
│   ├── main.py
│   ├── topology/
│   │   └── [topology files]
│   └── protocol_sim/
│       └── [protocol simulation files]
│
└── protocols/
    ├── ospf.py
    ├── rip.py
    ├── bgp.py
    ├── isis.py
    └── aospf.py
```

### Directory Descriptions

| Directory | Description |
|-----------|-------------|
| `ASOPF/` | Standalone AOSPF protocol implementation with simulation tools |
| `ASOPF_comparison_with_isis_ospf_BGP_RIP/` | Comparative analysis module for multiple routing protocols |
| `protocols/` | Core protocol implementations used across the project |

## 💻 Usage

### Running AOSPF Comparison

To run the AOSPF protocol simulation:

```bash
cd ASOPF
python main.py
```

### Running All Protocols Comparison

To run comparative analysis with all implemented protocols (AOSPF, OSPF, IS-IS, BGP, RIP):

```bash
cd ASOPF_comparison_with_isis_ospf_BGP_RIP
python main.py
```

## 🌐 Protocols Implemented

### OSPF (Open Shortest Path First)
- Link-state routing protocol
- Suitable for medium to large networks
- Located in: `protocols/ospf.py`

### RIP (Routing Information Protocol)
- Distance-vector routing protocol
- Simpler but less efficient than OSPF
- Located in: `protocols/rip.py`

### BGP (Border Gateway Protocol)
- Path-vector routing protocol
- Used for inter-domain routing
- Located in: `protocols/bgp.py`

### IS-IS (Intermediate System to Intermediate System)
- Link-state routing protocol
- Similar to OSPF but different protocol design
- Located in: `protocols/isis.py`

### AOSPF (Experimental Protocol)
- Custom routing protocol implementation
- Located in: `protocols/aospf.py`

## 🤝 Contributing

This project was developed by **Team Synex** with contributions from:

- **Dulith Kavinda**
- **Achintha**
- **Ravindu**
- **Thejake**

## 📜 License

This project is currently **unlicensed**. Please see the [LICENSE](LICENSE) file for more information.

## 📧 Contact

For questions, suggestions, or issues, please:

- Open an [issue](https://github.com/Dulith-Kavinda/network_Protocol_design/issues) in this repository
- Contact the development team through GitHub

---

**Last Updated:** May 17, 2026  
**Language:** Python 3.x  
**Repository:** [Dulith-Kavinda/network_Protocol_design](https://github.com/Dulith-Kavinda/network_Protocol_design)
