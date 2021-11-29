// Gmsh project


lc = 1e-2;
ld = 1e-3;

Point(1) = {0.02, 0, 0, ld};
Point(2) = {0.1, 0, 0, lc};
Point(3) = {0.1, 0.05, 0, lc};
Point(4) = {0, 0.05, 0, lc};
Point(5) = {0, 0.02, 0, ld};
Point(6) = {0, 0, 0, lc};

Line(1)= {1, 2};
Line(2)= {2, 3};
Line(3)= {3, 4};
Line(4)= {4, 5};
Circle(5) = {5, 6, 1};

Curve Loop(1) = {3, 4, 5, 1, 2};
Plane Surface(1) = {1};

Physical Curve("Left") = {4};
Physical Curve("Right") = {2};
Physical Curve("Bottom") = {1};
Physical Surface("Plate_surf") = {1};

Save "simpleplate.unv";