#definition de la fonction avant execution
def pts_to_xyz_with_rgb(pts_filename, xyz_filename):
    #ouvrir et lire le pts, et ouvrir un fichier .xyz
    with open(pts_filename, 'r') as pts_file, open(xyz_filename, 'w') as xyz_file:
        #lire lignes du pts
        for line in pts_file:

            parts = line.split()

            xyz = parts[:6]

            xyz_file.write(' '.join(xyz ) + '\n')

#execution
pts_filename = r"C:\Users\naim.cheriguene\OneDrive - HEJAUS\Documents - Etudes Techniques\Modélisation 3D BIM\03-2024\PJ - R&D BIM CLOUD\PJ- RD DIAGRENT - 01_clean.pts"
xyz_filename = r"C:\Users\naim.cheriguene\OneDrive - HEJAUS\Documents - Etudes Techniques\Modélisation 3D BIM\03-2024\PJ - R&D BIM CLOUD\full_cloud-points_clean.xyz"
pts_to_xyz_with_rgb(pts_filename, xyz_filename)
