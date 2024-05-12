# GlusterFS Prometheus node exporter (Fedora 40)

Минимальный набор сборки rpm-пакета для Fedora 40. Т.к. оригинальный пакет сложен и в виду того, что обновлены зависимости - вообще не собирается, был создан этот репозиторий.

- Оригинал: https://github.com/gluster/gluster-prometheus
- go.mod позаимствован отсюда: https://github.com/robertlestak/gluster-prometheus

## Сборка:

```bash
sudo dnf install git -y
```

```bash
git clone https://github.com/KasperWPS/gluster-exporter.git
```
```bash
cd gluster-exporter
```
```bash
./build.sh
```

- При успешной сборке rpm-пакет будет в: **~/rpmbuild/RPMS/x86_64/gluster-exporter-1.0-2.fc40.x86_64.rpm**