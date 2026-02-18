package abc430;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

class ETest {

    private static String stripLastNewline(String s) {
        // 末尾の改行だけを1個除去（\n / \r\n 対応）
        return s.replaceFirst("\\R\\z", "");
    }

    private static String show(String s) {
        // 見比べやすい表示（改行を可視化）
        return s.replace("\r", "\\\\r").replace("\n", "⏎\\n");
    }


    @Test
    void sample1() {
        String input = "5\n1010001\n1000110\n000\n111\n01010\n01010\n0101\n0011\n100001101110000001010110110001\n101100011000011011100000010101";
        String expected = "2\n-1\n0\n-1\n22";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            E.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


}
