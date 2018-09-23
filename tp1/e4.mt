function [] = normal(N, media, desvio)

c = sqrt(2*exp(1)/pi);
t = exprnd(1,1,N);    % Generamos un vector de 1xN muestras
p = fX(t, media, desvio)./(c*fY(t, media)); % Probabilidad de aceptar
z= [];
for n=1:N
    r = rand();
    if r < p(n) % acepto t(n) con prob. p(n)
        r2 = rand();
        if r2 < 0.5 % con prob 0.5 lo dejo positivo
            z = [z, t(n)];
        else  % con prob 0.5 lo hago negativo
            z = [z, -t(n)];
        end
    end 
end

disp(['Porcentaje de rechazo = ', num2str((N-length(z))/N)])

% Mostramos histograma del resultado
figure
histogram(z, N)

end

% Exponencial
function f = fY(y, media)
f = exp(-y*media);
end

% Gaussiana
function f = fX(x, media, desvio)
f = exp(-(x - media).^2/(2*desvio.^2))/(sqrt(2*pi)*desvio);
end
