# Assignment 5

This repository contains the implementations and conceptual answers for assignment 5 programming part. The repository covers search algorithms, knowledge-base reasoning, knowledge graphs, and probabilistic modeling using Bayesian networks.

---

## Question 1: Search Algorithms

### Description

This module implements four key search algorithms (Minimax, Alpha-Beta Pruning, Heuristic Alpha-Beta, and Monte-Carlo Tree Search) evaluated within a generic Tic-Tac-Toe environment.

### How to Run

Execute the file using Python:
```bash
python search_algorithms.py
```

### Output

The script runs three distinct tests:

* Test 1 demonstrates Minimax and Alpha-Beta finding an immediate winning move.
* Test 2 shows Heuristic Alpha-Beta successfully blocking an opponent's win at a limited depth.
* Test 3 uses Monte-Carlo Tree Search to simulate 1000 games and pick the optimal starting move on an empty board.

The output displays the visual state of the board before and after the AI makes its decision.

---

## Question 2: AI Travel Planner

### Description

An automated travel planning engine that utilizes interconnected domain knowledge bases (Tourist Places, Wine Ontology, and Food Recommendations). It acts as a semantic matcher and cost assessor to build itineraries based on user constraints.

### How to Run

Execute the file using Python:
```bash
python travel_planner.py
```

### Output

The script processes a sample user profile (luxury budget, 3 days, interested in history and wine) and outputs a human-readable travel report. This includes a total cost breakdown, matched destination details, domain knowledge applications (must-try dishes, regional wine pairings), and a day-by-day activity plan.

---

## Question 3: Knowledge Graphs and Tools

### What is a Knowledge Graph?

A Knowledge Graph (KG) is a computational representation of real-world entities, concepts, and the complex relationships between them. Unlike traditional relational databases that store data in rigid tables and columns, a Knowledge Graph stores data as a network. This structure allows systems to capture both the data itself and the contextual meaning (semantics) behind it, making it highly effective for AI reasoning, search engines, and recommendation systems.

### Core Components of a Knowledge Graph

* Nodes (Entities): Represent individual objects, concepts, or events (e.g., "Leonardo da Vinci", "Mona Lisa", "Painting").
* Edges (Relationships): The semantic links connecting two nodes, defining how they interact (e.g., "painted", "is_a").
* Properties: Attributes or metadata attached to nodes or edges (e.g., "creation_year: 1503").
* Ontology: The underlying schema or rulebook that defines the classes, hierarchies, and allowable relationships within the specific domain.

### Tools for Building Knowledge Graphs

Building a Knowledge Graph requires a combination of storage, modeling, and data extraction tools. They are generally categorized as follows:

#### 1. Graph Databases (Storage & Querying)

* Neo4j: The most widely adopted native graph database. It uses Property Graphs and the Cypher query language, making it highly optimized for deep link traversal and pattern matching.
* Amazon Neptune: A fully managed cloud database by AWS that supports both major graph architectures: Property Graphs (using Apache TinkerPop Gremlin) and RDF graphs (using SPARQL).
* TigerGraph: A distributed, native graph database designed for massive scale and advanced analytics, utilizing the GSQL query language.

#### 2. Ontology and Taxonomy Editors (Modeling)

* Protégé: A free, open-source ontology editor developed by Stanford University. It is the industry standard for creating complex domain models and supports the Web Ontology Language (OWL).

#### 3. Data Integration and Processing Frameworks

* Apache Jena: A robust, open-source Java framework specifically designed for building Semantic Web and Linked Data applications. It provides an API to extract data from and write to RDF graphs.
* TypeDB (formerly Grakn): A strongly-typed database tailored for knowledge engineering. It features a highly expressive schema language and a built-in reasoning engine that can automatically infer new relationships from existing data.

---

## Question 4: Bayesian Networks

### Description

This module explores probabilistic graphical modeling using the pgmpy library. It implements Judea Pearl's classic "Burglar Alarm" scenario using a DiscreteBayesianNetwork to model the conditional dependencies between a burglary, an earthquake, an alarm, and neighbors calling.

### How to Run

First, install the required dependency:
```bash
pip install pgmpy
```

Then, execute the file:
```bash
python bayesian_network.py
```

### Output

The script runs a variable elimination inference engine to answer two specific queries:

* The probability of a burglary occurring given that both neighbors (John and Mary) called.
* The probability of the alarm sounding if there is a confirmed earthquake but no burglary.

The output prints the exact probability distributions for both scenarios.
