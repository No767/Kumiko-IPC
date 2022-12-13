<div align=center>

# Kumiko-IPC

![Kumiko's Logo](https://raw.githubusercontent.com/No767/Kumiko/dev/assets/kumiko-resized-round.png)

[![Required Python Version](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-blue?logo=python&logoColor=white)](https://github.com/No767/Kumiko-IPC/blob/dev/pyproject.toml) [![GitHub License](https://img.shields.io/github/license/No767/Kumiko-IPC?label=License&logo=github)](https://github.com/No767/Kumiko-IPC/blob/dev/LICENSE)

Kumiko's Custom IPC Workers

<div align=left>

## Info
This github repo hosts the source code for Kumiko's IPC worker. The IPC worker uses Celery in order to spilt the workloads into manageable tasks, which then only get sent to Kumiko. This creates a distrbuted workload, therefore spreading out the load and helping with performance. 

## Checklist for features

- [ ] Implement Celery Workers
- [ ] Docker Support
- [ ] Prometheus Metrics

## License

[GPL-3.0](./LICENSE)
