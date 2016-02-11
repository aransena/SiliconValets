function[image] = infile_read(file_name)
EOL = 10;
LO = 46;
HI = 35;
fileID = fopen(file_name,'r');
row_col = importdata(file_name);
num_rows = row_col(1);
num_cols = row_col(2);
fgets(fileID);
delim_raster_image = fread(fileID);
raster_image = delim_raster_image(delim_raster_image~=EOL);
fclose(fileID);
image = reshape(raster_image,num_cols,num_rows);
image(image==LO) = 0;
image(image==HI) = 255;
image = image';
end

