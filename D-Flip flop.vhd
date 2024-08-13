library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity D_flipflop is
    Port (
        D   : in  STD_LOGIC;  -- Input D
        Clk : in  STD_LOGIC;  -- Clock input
        Q   : out STD_LOGIC   -- Output Q
    );
end D_flipflop;

architecture Behavioral of D_flipflop is
begin
    process(Clk)
    begin
        if rising_edge(Clk) then
            Q <= D;  -- Assign D to Q on the rising edge of Clk
        end if;
    end process;
end Behavioral;