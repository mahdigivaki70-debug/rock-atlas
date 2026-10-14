package ir.rockatlas.ui

import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.material.icons.outlined.Language
import androidx.compose.material.icons.outlined.Phone
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.TextButton
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AboutScreen(onBack: () -> Unit) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("درباره، سازنده و منابع") },
                navigationIcon = { IconButton(onClick = onBack) { Icon(Icons.AutoMirrored.Filled.ArrowBack, "بازگشت") } },
            )
        },
    ) { pad ->
        Column(Modifier.padding(top = pad.calculateTopPadding()).verticalScroll(rememberScrollState()).padding(16.dp)) {
            CreditsCard()
            Spacer(Modifier.height(8.dp))
            Para("اطلس سنگ‌های ساختمانی، راهنمای آفلاین سنگ‌های نما و کف ایران و جهان است: نوع سنگ، رنگ، معدن و منطقه، کاربرد، فرآوری سطح و مشخصات آزمایشگاهی.")
            Head("مشخصات آزمایشگاهی")
            Para("اعداد چگالی، جذب آب، مقاومت فشاری و خمشی و سختی، محدودهٔ معمول هر نوع سنگ بر پایهٔ استانداردهای ASTM برای سنگ ساختمانی (C615، C503، C1527، C568، C616، C629، C1526) و منابع عمومی است. این‌ها نتیجهٔ آزمایش معدن خاصی نیستند و برای طراحی سازه باید گزارش آزمون همان محموله را گرفت.")
            Head("تصاویر")
            Para("تصاویر هنگام اتصال به اینترنت از ویکی‌مدیا کامانز (از طریق ویکی‌پدیا) دریافت و روی گوشی ذخیره می‌شوند. فقط تصاویر با مجوز آزاد کامانز نمایش داده می‌شوند و زیر هر تصویر پیوند صفحهٔ فایل، شامل نام پدیدآورنده و مجوز، آمده است. اگر برای سنگی تصویر اختصاصی نباشد، تصویر نمونهٔ همان نوع سنگ با برچسب «تصویر نمونه» نشان داده می‌شود.")
            Head("شناسایی با عکس")
            Para("شناسایی کاملاً روی گوشی انجام می‌شود و عکس شما به هیچ سروری ارسال نمی‌شود. رنگ و بافت عکس به همراه آزمون‌های ساده با بانک اطلاعاتی مقایسه می‌شود. گوگل لنز API عمومی ندارد؛ دکمهٔ «پرسیدن از گوگل لنز» فقط عکس را به اپ لنز روی گوشی شما می‌دهد.")
            Head("حریم خصوصی و امنیت")
            Para("اپ فقط مجوز اینترنت دارد (برای عکس‌ها)، فقط با HTTPS و فقط با دامنه‌های ویکی‌پدیا و ویکی‌مدیا ارتباط می‌گیرد، هیچ حساب کاربری، تبلیغ یا ردیاب ندارد و اطلاعات مکان (EXIF) را از عکس‌ها حذف می‌کند.")
        }
    }
}

@Composable
fun CreditsCard() {
    val context = LocalContext.current
    Card(
        modifier = Modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.primaryContainer),
    ) {
        Column(Modifier.padding(16.dp)) {
            Text("سازنده", style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary)
            Text(Credits.AUTHOR, style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(8.dp))
            TextButton(onClick = { dial(context, Credits.PHONE) }) {
                Icon(Icons.Outlined.Phone, null)
                Spacer(Modifier.width(8.dp))
                // Phone numbers read left-to-right even inside Persian text.
                Text("\u2066${Credits.PHONE}\u2069")
            }
            TextButton(onClick = { openHttps(context, Credits.WEBSITE_URL) }) {
                Icon(Icons.Outlined.Language, null)
                Spacer(Modifier.width(8.dp))
                Text(Credits.WEBSITE)
            }
        }
    }
}

object Credits {
    const val AUTHOR = "مهدی گیوکی"
    const val PHONE = "+989192950266"
    const val WEBSITE = "www.nexstone.ir"
    const val WEBSITE_URL = "https://www.nexstone.ir"
}

/** Opens the dialer with the number filled in; needs no CALL_PHONE permission. */
private fun dial(context: Context, phone: String) {
    try {
        context.startActivity(Intent(Intent.ACTION_DIAL, Uri.fromParts("tel", phone, null)))
    } catch (e: ActivityNotFoundException) {
    }
}

@Composable
private fun Head(t: String) = Text(t, style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary, modifier = Modifier.padding(top = 16.dp, bottom = 4.dp))

@Composable
private fun Para(t: String) = Text(t, style = MaterialTheme.typography.bodyMedium)
