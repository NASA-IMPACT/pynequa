# Pynequa
A python library to handle communication with Sinequa REST API. 

[![Documentation Status](https://readthedocs.org/projects/pynequa/badge/?version=latest)](https://pynequa.readthedocs.io/en/latest/?badge=latest)
![Build](https://github.com/NASA-IMPACT/pynequa/actions/workflows/pkg_build_check.yml/badge.svg)

> Sinequa is an enterprise search tool. It provides a cognitive search and analytics platform that helps organizations gain insights from their structured and unstructured data spread across various sources, including databases, documents, emails, websites, and more.

## Installation 

```
   $ pip install pynequa
```
## Feature Roadmap 
Implement following REST endpoints to manage requests with Sinequa API. 

**Search Endpoints:**
- [x] search.app 
- [x] search.dataset
- [x] search.query
- [x] queryintent
- [x] search.profile
- [x] search.usersettings
- [x] search.preview
- [x] search.queryexport
- [x] search.recentqueries
- [x] search.similardocuments
- [x] search.querylinks
- [x] search.ratings
- [x] search.profile.subtree
- [ ] search.alerts
- [ ] search.baskets
- [ ] search.labels
- [ ] serach.savedQueries
- [ ] search.suggest
- [ ] search.custom
- [ ] suggestField
- [ ] engine.sql 

**Indexing Endpoints**
- [ ] indexing.collection
- [ ] indexing.customCollection
- [ ] indexing.partition 

**Operating Task Endpoints**
- [ ] operation.actionStatus
- [ ] operation.collectionStart
- [ ] operation.commandStart
- [ ] operation.jobStart
- [ ] operation.partitionStart
- [ ] operation.server
- [ ] operation.serverstatus
- [ ] operation.taskstatus

**General Endpoints**
- [ ] audit.notify
- [ ] admin.config 
- [ ] dev.plugin 
- [ ] multi 

## Development
Check [DEVELOPERS GUIDE](DEVELOPMENT.md) for details. 
## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the authors of this repository before making a change. 

## License

Distributed under the terms of the [MIT license](LICENSE),
`pynequa` is free and open source software.

