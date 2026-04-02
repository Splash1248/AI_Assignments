from CSP import solve_csp

try:
    import geopandas as gpd
    import matplotlib.pyplot as plt
except ImportError:
    print("----------------------")
    print("Missing libraries: matplotlib and geopandas are missing. Install them with the following:")
    print("pip install matplotlib geopandas")
    exit(1)


gdf = gpd.read_file("districts.geojson")

dist_col = gdf.columns[0]
for col in ['Name', 'JNAME', 'Dist_Name', 'DISTRICT', 'District']:
    if col in gdf.columns:
        dist_col = col
        break

vars = gdf[dist_col].tolist()
doms = {v: ['#FF9999', '#99FF99', '#9999FF', '#FFFF99'] for v in vars}

nbrs = {}
for idx, row in gdf.iterrows():
    intersecting = gdf[gdf.geometry.touches(row.geometry)]
    nbrs[row[dist_col]] = intersecting[dist_col].tolist()


ans = solve_csp(vars, doms, nbrs)

gdf['color'] = gdf[dist_col].map(ans)

fig, ax = plt.subplots(figsize=(12, 12))
gdf.plot(color=gdf['color'], edgecolor='black', ax=ax)

for _, row in gdf.iterrows():
    pt = row.geometry.centroid
    ax.text(pt.x, pt.y, row[dist_col], ha='center', va='center', fontsize=6)

ax.axis('off')
plt.show()
