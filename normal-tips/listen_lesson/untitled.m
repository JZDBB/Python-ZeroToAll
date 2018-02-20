a = imread('screenshot.png');
a = mean(a, 3);
% imshow(uint8(a))
b = a(270:-1:230,50:-1:8);
% b = a(230:270,8:50);
c = filter2(b, a, 'full');
c = c/max(max(c))*255;
% c = uint8(c==max(max(c)));
% for i = 1:808
%     x = find(c(i,:) ~= 0);
%     if sum(x ~= 0)
%         i
%         find(x ~= 0)
%     end
% end
imshow(uint8(c))
% [max_num, id] = max(c);
% d = max(c);
% [max_num2, id2] = max(d);
% id = id(id2);
% imshow(uint8(a))
