%% Description
%Creates set of 2-dimensional grid vectors with length and width (i,j).
%i and j are taken no large than M.
%Makes sure there are no vectors with same slope (ex. no (1,2) and (2,4)).
%% Function
function V = gridvectors(M)
    V1=[];
    for i = 1 : M
        for j = 0 : i
            if ~(i == 0 && j == 0)
                V1 = [V1; i j];
            end
        end
    end
    [v,ind,~] = unique(V1(:,2)./V1(:,1),'first'); %eliminates same slope vectors
    V1 = V1(sort(ind),:);

    V2 = [V1(:,2) V1(:,1)];

    V = zeros(2*size(V1,1),2);

    V(1:2:size(V,1),:) = V1;
    V(2:2:size(V,1),:) = V2;
    V = [V(1:2,:);V(4:end,:)];
end
